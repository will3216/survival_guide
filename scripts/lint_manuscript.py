"""Structural validation for the manuscript.

Every rule is a function returning a list of error strings. An empty
return means clean. Front matter (00-) and appendices (99-) are exempt;
rules apply to the numbered chapters listed in notes/manuscript-order.txt.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from illo_blocks import strip_comments

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


def lint(root: Path) -> list[str]:
    errors: list[str] = []
    for name in read_order(root):
        path = root / "manuscript" / name
        if not path.exists():
            errors.append(_err(name, "MISSING", "listed in manuscript-order.txt but not written yet"))
            continue
        text = path.read_text()
        for rule in CHAPTER_RULES:
            errors.extend(rule(name, text))
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
