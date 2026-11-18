"""Structural validation for the manuscript.

Every rule is a function returning a list of error strings. An empty
return means clean. Front matter (00-) and appendices (99-) are exempt;
rules apply to the numbered chapters listed in notes/manuscript-order.txt.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from illo_blocks import ID_RE, parse_blocks, strip_comments

WORDS_MIN = 1800
WORDS_MAX = 3200
SHORT_MIN = 5
SHORT_MAX = 9
EPIGRAPH_WITHIN_LINES = 12

COSTS_HEADING = "## What It Costs You"
SHORT_HEADING = "## The Short Version"


def _err(name: str, rule: str, message: str) -> str:
    return f"{name}: {rule}: {message}"


def read_order(root: Path) -> list[str]:
    path = root / "notes" / "manuscript-order.txt"
    lines = path.read_text().splitlines()
    return [l.strip() for l in lines if l.strip() and not l.startswith("#")]


def check_epigraph(name: str, text: str) -> list[str]:
    lines = text.splitlines()
    head = lines[1 : EPIGRAPH_WITHIN_LINES + 1]
    if any(l.strip().startswith("> ") for l in head):
        return []
    return [
        _err(
            name,
            "EPIGRAPH",
            f"no blockquote epigraph within the first {EPIGRAPH_WITHIN_LINES} lines",
        )
    ]


def check_costs_section(name: str, text: str) -> list[str]:
    if COSTS_HEADING in text:
        return []
    return [_err(name, "COSTS", f"missing '{COSTS_HEADING}' section")]


def check_short_version(name: str, text: str) -> list[str]:
    if SHORT_HEADING not in text:
        return [_err(name, "SHORT", f"missing '{SHORT_HEADING}' section")]
    tail = text.split(SHORT_HEADING, 1)[1]
    bullets = [l for l in tail.splitlines() if l.strip().startswith("- ")]
    count = len(bullets)
    if SHORT_MIN <= count <= SHORT_MAX:
        return []
    return [
        _err(
            name,
            "SHORT",
            f"has {count} bullets, needs {SHORT_MIN}-{SHORT_MAX}",
        )
    ]


def check_word_count(name: str, text: str) -> list[str]:
    words = len(strip_comments(text).split())
    if WORDS_MIN <= words <= WORDS_MAX:
        return []
    return [
        _err(name, "WORDS", f"{words} words, needs {WORDS_MIN}-{WORDS_MAX}")
    ]


CHAPTER_RULES = (
    check_epigraph,
    check_costs_section,
    check_short_version,
    check_word_count,
)

REQUIRED_ILLO_KEYS = ("id", "class", "caption", "alt", "prompt")
RULE_CITE_RE = re.compile(r"\bRule (\d{1,3})\b")
LEDGER_ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")
ACCURACY_HEADING_RE = re.compile(r"^##\s*Chapter\s*(\d{2})", re.MULTILINE)


def check_illo_blocks(name: str, text: str) -> list[str]:
    errors: list[str] = []
    prefix = name[:2]
    for block in parse_blocks(text):
        where = f"ILLO at line {block.line}"
        missing = [k for k in REQUIRED_ILLO_KEYS if k not in block.raw_keys or not block.raw_keys[k]]
        if missing:
            errors.append(_err(name, "ILLO", f"{where} missing key(s): {', '.join(missing)}"))
        unknown = [k for k in block.raw_keys if k not in REQUIRED_ILLO_KEYS]
        if unknown:
            errors.append(_err(name, "ILLO", f"{where} has unexpected key(s): {', '.join(unknown)}"))
        match = ID_RE.match(block.id)
        if not match:
            errors.append(_err(name, "ILLO", f"{where} id '{block.id}' must look like 04-plate-01 or 04-gag-02"))
            continue
        chapter_no, token, _ = match.groups()
        if chapter_no != prefix:
            errors.append(_err(name, "ILLO", f"{where} id prefix '{chapter_no}' does not match chapter prefix '{prefix}'"))
        if block.cls != token:
            errors.append(_err(name, "ILLO", f"{where} class '{block.cls}' disagrees with id token '{token}'"))
        expected = f"](../illustrations/{block.id}.png)"
        if not any(l.startswith("![") and expected in l for l in block.following_lines):
            errors.append(_err(name, "ILLO", f"{where} is not followed by its image link ending '{expected}'"))
    return errors


def check_forbidden(name: str, text: str, terms: list[str]) -> list[str]:
    errors: list[str] = []
    lowered = text.lower()
    for term in terms:
        if term.lower() in lowered:
            errors.append(_err(name, "FORBIDDEN", f"contains '{term}'"))
    return errors


def check_rules_cited(name: str, text: str, ledger: set[int]) -> list[str]:
    errors: list[str] = []
    for number in sorted({int(n) for n in RULE_CITE_RE.findall(text)}):
        if number not in ledger:
            errors.append(_err(name, "RULE", f"cites Rule {number}, which is not in the continuity.md ledger"))
    return errors


def read_forbidden(root: Path) -> list[str]:
    path = root / "notes" / "forbidden-terms.txt"
    if not path.exists():
        return []
    lines = path.read_text().splitlines()
    return [l.strip() for l in lines if l.strip() and not l.startswith("#")]


def read_rule_ledger(root: Path) -> set[int]:
    path = root / "notes" / "continuity.md"
    if not path.exists():
        return set()
    numbers = set()
    for line in path.read_text().splitlines():
        match = LEDGER_ROW_RE.match(line.strip())
        if match:
            numbers.add(int(match.group(1)))
    return numbers


def read_accuracy_chapters(root: Path) -> set[str]:
    path = root / "notes" / "accuracy-log.md"
    if not path.exists():
        return set()
    return set(ACCURACY_HEADING_RE.findall(path.read_text()))


def lint(root: Path) -> list[str]:
    errors: list[str] = []
    forbidden = read_forbidden(root)
    ledger = read_rule_ledger(root)
    logged = read_accuracy_chapters(root)
    seen_illo_ids: dict[str, str] = {}

    for name in read_order(root):
        path = root / "manuscript" / name
        if not path.exists():
            errors.append(_err(name, "MISSING", "listed in manuscript-order.txt but not written yet"))
            continue
        text = path.read_text()
        for rule in CHAPTER_RULES:
            errors.extend(rule(name, text))
        errors.extend(check_illo_blocks(name, text))
        errors.extend(check_forbidden(name, text, forbidden))
        errors.extend(check_rules_cited(name, text, ledger))

        if name[:2] not in logged:
            errors.append(_err(name, "ACCURACY", f"no '## Chapter {name[:2]}' heading in notes/accuracy-log.md"))

        for block in parse_blocks(text):
            if block.id in seen_illo_ids:
                errors.append(_err(name, "DUPLICATE", f"ILLO id '{block.id}' already used in {seen_illo_ids[block.id]}"))
            else:
                seen_illo_ids[block.id] = name

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = lint(root)
    for error in errors:
        print(error)
    if errors:
        print(f"\n{len(errors)} problem(s).")
        return 1
    print("Manuscript clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
