# The Long After Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write *The Long After* — a 20-chapter, 45k–55k word satirical-but-practical post-apocalyptic survival guide in Markdown, with illustration slots and prompts placed throughout but no images generated yet.

**Architecture:** Two small Python tools are built first — a manuscript linter and an illustration-manifest collector — so that every prose chapter has an objective, automated pass/fail gate covering apparatus completeness, word count, illustration-slot validity, accuracy-log coverage, and Rule-ledger consistency. Three reference documents (style guide, continuity bible, illustration style guide) are written next and then obeyed. Chapters are drafted in spec order, one commit each, with a human review checkpoint at the end of each Part.

**Tech Stack:** Markdown (manuscript), Python 3.12.10 via asdf (tooling), pytest 8.2.2, standard library only — no third-party runtime dependencies.

**Spec:** `docs/superpowers/specs/2026-11-17-long-after-design.md`

## Global Constraints

- **The narrator is never ironic about technique.** Comedy comes from framing, anecdote, and his sense of what is normal — never from giving the reader bad information.
- **No invented numbers.** Treatment ratios, tourniquet placement, water and calorie minimums, food-preservation safety, and fuel storage life come from established real-world guidance or they do not appear. Where guidance is contested, take the conservative position and say why. Anything uncertain is written vaguer rather than wronger.
- **Every load-bearing factual claim gets an entry in `notes/accuracy-log.md`** under that chapter's heading, naming the real-world basis.
- **Off the page regardless of framing:** weapons and explosives manufacture; operationalized coercive-control technique. Cults are handled as failure modes to recognize.
- **Tone register:** mostly light with a dark undertow. At most **one** dark aside per chapter, dropped and not revisited.
- **Tone touchstones:** Zombieland governs voice, violence, and instructiveness. Mad Max governs world only. No proper nouns from either.
- **No *Mad Max* or *Zombieland* proper nouns.** Every faction, god, place, and person is original.
- **Chapter word count:** 1,800–3,200 words, excluding HTML comment blocks.
- **Per-chapter apparatus, all five, every chapter:** epigraph; ~300-word opening with one named person; the instruction; `## What It Costs You`; `## The Short Version` (5–9 bullets).
- **The prose stands alone.** Every chapter must read correctly with zero images present.
- **Illustration budget:** ~3 slots per chapter, roughly 1 `plate` and 2 `gag`.
- **Rules are real advice compressed.** Never invented to be funny at the expense of being true. Every Rule cited in a chapter must exist in the `notes/continuity.md` Rule ledger.

---

## File Structure

| Path | Responsibility |
|------|----------------|
| `notes/manuscript-order.txt` | The authoritative list of chapter filenames. Single source of truth for "what chapters exist"; drives the linter's missing-file check. |
| `notes/forbidden-terms.txt` | Proper nouns that must never appear. One per line. |
| `notes/style-guide.md` | Voice rules, the apparatus template, the tone-touchstone calibration. |
| `notes/continuity.md` | Cast, factions, gods, timeline, and the authoritative Rule ledger. |
| `notes/illustration-style.md` | The fixed prompt preamble, palette, do-not list, character and object sheets. |
| `notes/accuracy-log.md` | Per-chapter real-world basis for every load-bearing claim. |
| `notes/illustration-manifest.json` | Generated. Batch input for image generation. |
| `scripts/lint_manuscript.py` | All manuscript structural validation. One rule per function, each returning a list of error strings. |
| `scripts/collect_illos.py` | Extracts `ILLO` blocks into the manifest. Shares the block parser with the linter. |
| `scripts/illo_blocks.py` | The `ILLO` comment-block parser. Shared by the linter and the collector so they can never disagree about what a valid block is. |
| `manuscript/00-front-matter.md` | Real-voice author's note, fictional editor's preface, contents. |
| `manuscript/NN-slug.md` | One chapter each, 20 files. |
| `manuscript/99-appendices.md` | The Rules appendix, reference tables, god-design worksheet. |
| `tests/test_illo_blocks.py` | Block parser tests. |
| `tests/test_lint_manuscript.py` | Linter rule tests. |
| `tests/test_collect_illos.py` | Collector tests. |

Front matter (`00-`) and appendices (`99-`) are exempt from the apparatus and word-count rules; the linter applies those only to numbered chapter files listed in `manuscript-order.txt`.

---

## Task 1: Repo scaffolding and the ILLO block parser

**Files:**
- Create: `scripts/illo_blocks.py`
- Create: `tests/test_illo_blocks.py`
- Create: `notes/manuscript-order.txt`
- Create: `notes/forbidden-terms.txt`
- Create: `.gitignore`
- Create: `README.md`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `illo_blocks.parse_blocks(text: str) -> list[IlloBlock]` — finds every `<!-- ILLO ... -->` comment in a Markdown string and returns parsed blocks in document order.
  - `IlloBlock` — a dataclass with fields `id: str`, `cls: str`, `caption: str`, `alt: str`, `prompt: str`, `raw_keys: dict[str, str]`, `line: int` (1-indexed line of the `<!-- ILLO` opener), `following_lines: list[str]` (the next 3 non-empty lines after the block closes).
  - `illo_blocks.strip_comments(text: str) -> str` — removes all HTML comments, used by the word-count rule.
  - `illo_blocks.ID_RE` — the compiled id pattern `^(\d{2})-(plate|gag)-(\d{2})$`.

- [ ] **Step 1: Create the scaffolding files**

`.gitignore`:

```
__pycache__/
*.pyc
.pytest_cache/
.venv/
illustrations/*.png
```

`notes/manuscript-order.txt`:

```
# The authoritative chapter list. One filename per line, in reading order.
# The linter errors on any file listed here that does not exist.
01-triage.md
02-run-or-dig-in.md
03-body.md
04-water.md
05-weather.md
06-food.md
07-first-people.md
08-gear.md
09-scavenging.md
10-machine.md
11-voices.md
12-rot.md
13-growing.md
14-economy.md
15-groups.md
16-grief.md
17-silhouette.md
18-gods.md
19-holidays.md
20-teaching.md
```

`notes/forbidden-terms.txt`:

```
# Proper nouns that must never appear in the manuscript.
# Matched case-insensitively as whole words/phrases.
Immortan
Furiosa
Rockatansky
Gas Town
Gastown
Bullet Farm
The Citadel
Thunderdome
War Boy
War Boys
Aunty Entity
Columbus
Tallahassee
Zombieland
Mad Max
```

`README.md`:

```markdown
# The Long After

A satirical but practical post-apocalyptic survival guide.
The book is funny. The advice is real.

- Spec: `docs/superpowers/specs/2026-11-17-long-after-design.md`
- Plan: `docs/superpowers/plans/2026-11-17-long-after.md`
- Manuscript: `manuscript/`
- Reference documents: `notes/`

## Checks

```bash
python3 scripts/lint_manuscript.py          # structural validation
python3 scripts/collect_illos.py            # regenerate the illustration manifest
python3 -m pytest tests/ -q                 # tool tests
```

Illustrations are not generated yet. Every slot carries its own prompt;
`notes/illustration-manifest.json` is the batch input for when they are.
```

- [ ] **Step 2: Write the failing tests**

`tests/test_illo_blocks.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import illo_blocks


VALID = """# Chapter Four

Some prose.

<!-- ILLO
id: 04-plate-01
class: plate
caption: Figure 4.1 - The three-stage filter.
alt: Cutaway of a layered gravel, sand, and charcoal filter.
prompt: Cutaway diagram of a three-layer water filter in a cut oil drum.
-->
![Figure 4.1 - The three-stage filter.](../illustrations/04-plate-01.png)

More prose.
"""


def test_parses_a_single_block():
    blocks = illo_blocks.parse_blocks(VALID)
    assert len(blocks) == 1
    b = blocks[0]
    assert b.id == "04-plate-01"
    assert b.cls == "plate"
    assert b.caption == "Figure 4.1 - The three-stage filter."
    assert b.alt.startswith("Cutaway of a layered")
    assert b.prompt.startswith("Cutaway diagram")


def test_records_the_opener_line_number():
    blocks = illo_blocks.parse_blocks(VALID)
    assert blocks[0].line == 5


def test_captures_following_lines_for_image_link_checks():
    blocks = illo_blocks.parse_blocks(VALID)
    assert blocks[0].following_lines[0].startswith("![Figure 4.1")


def test_parses_blocks_in_document_order():
    text = VALID + VALID.replace("04-plate-01", "04-gag-01").replace(
        "class: plate", "class: gag"
    )
    ids = [b.id for b in illo_blocks.parse_blocks(text)]
    assert ids == ["04-plate-01", "04-gag-01"]


def test_missing_keys_are_absent_not_fatal():
    text = "<!-- ILLO\nid: 04-gag-02\n-->\n"
    b = illo_blocks.parse_blocks(text)[0]
    assert b.id == "04-gag-02"
    assert b.cls == ""
    assert "caption" not in b.raw_keys


def test_ignores_ordinary_html_comments():
    assert illo_blocks.parse_blocks("<!-- just a note -->") == []


def test_strip_comments_removes_illo_blocks():
    out = illo_blocks.strip_comments(VALID)
    assert "ILLO" not in out
    assert "Some prose." in out


def test_id_pattern_accepts_plate_and_gag_only():
    assert illo_blocks.ID_RE.match("04-plate-01")
    assert illo_blocks.ID_RE.match("20-gag-03")
    assert not illo_blocks.ID_RE.match("04-marginalia-01")
    assert not illo_blocks.ID_RE.match("4-plate-1")
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_illo_blocks.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'illo_blocks'`

- [ ] **Step 4: Write the parser**

`scripts/illo_blocks.py`:

```python
"""Parser for ILLO illustration-slot comment blocks.

Shared by lint_manuscript.py and collect_illos.py so the two can never
disagree about what a valid slot looks like.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

ID_RE = re.compile(r"^(\d{2})-(plate|gag)-(\d{2})$")

_BLOCK_RE = re.compile(r"<!--\s*ILLO\b(.*?)-->", re.DOTALL)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_KEY_RE = re.compile(r"^([a-z_]+):\s*(.*)$")

_FOLLOWING_LINES = 3


@dataclass
class IlloBlock:
    id: str = ""
    cls: str = ""
    caption: str = ""
    alt: str = ""
    prompt: str = ""
    raw_keys: dict[str, str] = field(default_factory=dict)
    line: int = 0
    following_lines: list[str] = field(default_factory=list)


def _parse_keys(body: str) -> dict[str, str]:
    """Parse `key: value` lines, folding indented continuations into the
    previous value so long prompts can wrap."""
    keys: dict[str, str] = {}
    current: str | None = None
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = _KEY_RE.match(line)
        if match:
            current = match.group(1)
            keys[current] = match.group(2).strip()
        elif current:
            keys[current] = (keys[current] + " " + line).strip()
    return keys


def parse_blocks(text: str) -> list[IlloBlock]:
    lines = text.splitlines()
    blocks: list[IlloBlock] = []
    for match in _BLOCK_RE.finditer(text):
        keys = _parse_keys(match.group(1))
        start_line = text.count("\n", 0, match.start()) + 1
        end_line = text.count("\n", 0, match.end()) + 1
        following = [l.strip() for l in lines[end_line:] if l.strip()]
        blocks.append(
            IlloBlock(
                id=keys.get("id", ""),
                cls=keys.get("class", ""),
                caption=keys.get("caption", ""),
                alt=keys.get("alt", ""),
                prompt=keys.get("prompt", ""),
                raw_keys=keys,
                line=start_line,
                following_lines=following[:_FOLLOWING_LINES],
            )
        )
    return blocks


def strip_comments(text: str) -> str:
    return _HTML_COMMENT_RE.sub("", text)
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_illo_blocks.py -q`
Expected: PASS, 8 passed

- [ ] **Step 6: Commit**

```bash
git add .gitignore README.md notes/manuscript-order.txt notes/forbidden-terms.txt scripts/illo_blocks.py tests/test_illo_blocks.py
git commit -m "Add repo scaffolding and the ILLO block parser"
```

---

## Task 2: Linter — chapter presence, word count, and apparatus

**Files:**
- Create: `scripts/lint_manuscript.py`
- Create: `tests/test_lint_manuscript.py`

**Interfaces:**
- Consumes: `illo_blocks.strip_comments` from Task 1.
- Produces:
  - `lint_manuscript.lint(root: Path) -> list[str]` — returns every error string found; empty list means clean.
  - `lint_manuscript.main() -> int` — prints errors one per line, returns exit code 0 or 1.
  - Each rule as a standalone function taking `(name: str, text: str) -> list[str]`: `check_epigraph`, `check_costs_section`, `check_short_version`, `check_word_count`.
  - Error string format: `"<file>: <RULE>: <message>"`.

- [ ] **Step 1: Write the failing tests**

`tests/test_lint_manuscript.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint_manuscript as lint


def chapter(body_words: int = 2000, *, epigraph=True, costs=True, short=6) -> str:
    parts = ["# Chapter Four: Water", ""]
    if epigraph:
        parts += ["> Rule 9: Water first. Always.", ""]
    parts += [" ".join(["word"] * body_words), ""]
    if costs:
        parts += ["## What It Costs You", "", "It costs you time.", ""]
    if short is not None:
        parts += ["## The Short Version", ""]
        parts += [f"- Point {i}" for i in range(short)]
    return "\n".join(parts) + "\n"


def test_clean_chapter_has_no_errors():
    assert lint.check_epigraph("04-water.md", chapter()) == []
    assert lint.check_costs_section("04-water.md", chapter()) == []
    assert lint.check_short_version("04-water.md", chapter()) == []
    assert lint.check_word_count("04-water.md", chapter()) == []


def test_missing_epigraph_is_an_error():
    errors = lint.check_epigraph("04-water.md", chapter(epigraph=False))
    assert len(errors) == 1
    assert "EPIGRAPH" in errors[0]


def test_epigraph_must_be_near_the_top():
    text = "# Title\n\n" + "\n\n".join(["filler"] * 20) + "\n\n> Too late.\n"
    assert lint.check_epigraph("04-water.md", text) != []


def test_missing_costs_section_is_an_error():
    errors = lint.check_costs_section("04-water.md", chapter(costs=False))
    assert "COSTS" in errors[0]


def test_short_version_must_exist():
    errors = lint.check_short_version("04-water.md", chapter(short=None))
    assert "SHORT" in errors[0]


def test_short_version_rejects_too_few_bullets():
    errors = lint.check_short_version("04-water.md", chapter(short=4))
    assert "SHORT" in errors[0]
    assert "4" in errors[0]


def test_short_version_rejects_too_many_bullets():
    assert lint.check_short_version("04-water.md", chapter(short=10)) != []


def test_short_version_accepts_boundary_counts():
    assert lint.check_short_version("04-water.md", chapter(short=5)) == []
    assert lint.check_short_version("04-water.md", chapter(short=9)) == []


def test_word_count_rejects_a_thin_chapter():
    errors = lint.check_word_count("04-water.md", chapter(body_words=200))
    assert "WORDS" in errors[0]


def test_word_count_rejects_a_bloated_chapter():
    assert lint.check_word_count("04-water.md", chapter(body_words=4000)) != []


def test_word_count_ignores_comment_blocks():
    text = chapter(body_words=1900) + "<!-- ILLO\n" + ("prompt words " * 2000) + "\n-->\n"
    assert lint.check_word_count("04-water.md", text) == []


def test_lint_reports_chapters_listed_but_missing(tmp_path):
    (tmp_path / "notes").mkdir()
    (tmp_path / "manuscript").mkdir()
    (tmp_path / "notes" / "manuscript-order.txt").write_text(
        "# comment\n01-triage.md\n04-water.md\n"
    )
    (tmp_path / "notes" / "forbidden-terms.txt").write_text("")
    (tmp_path / "notes" / "accuracy-log.md").write_text("## Chapter 01\n")
    (tmp_path / "notes" / "continuity.md").write_text("")
    (tmp_path / "manuscript" / "01-triage.md").write_text(chapter())
    errors = lint.lint(tmp_path)
    assert any("MISSING" in e and "04-water.md" in e for e in errors)
    assert not any("01-triage.md" in e and "MISSING" in e for e in errors)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_lint_manuscript.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'lint_manuscript'`

- [ ] **Step 3: Write the linter**

`scripts/lint_manuscript.py`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_lint_manuscript.py -q`
Expected: PASS, 12 passed

- [ ] **Step 5: Run the linter against the real repo**

Run: `python3 scripts/lint_manuscript.py`
Expected: exit 1, with 20 `MISSING` lines — one per unwritten chapter. This is the red state the whole manuscript is written against.

- [ ] **Step 6: Commit**

```bash
git add scripts/lint_manuscript.py tests/test_lint_manuscript.py
git commit -m "Add manuscript linter: presence, word count, apparatus"
```

---

## Task 3: Linter — illustration slots, forbidden terms, accuracy log, Rule ledger

**Files:**
- Modify: `scripts/lint_manuscript.py`
- Modify: `tests/test_lint_manuscript.py`

**Interfaces:**
- Consumes: `illo_blocks.parse_blocks`, `illo_blocks.ID_RE` from Task 1; `lint_manuscript.lint` from Task 2.
- Produces:
  - `check_illo_blocks(name: str, text: str) -> list[str]` — per-chapter slot validity.
  - `check_forbidden(name: str, text: str, terms: list[str]) -> list[str]`
  - `check_rules_cited(name: str, text: str, ledger: set[int]) -> list[str]`
  - `read_forbidden(root) -> list[str]`, `read_rule_ledger(root) -> set[int]`, `read_accuracy_chapters(root) -> set[str]`
  - `RULE_CITE_RE` — `re.compile(r"\bRule (\d{1,3})\b")`
  - `LEDGER_ROW_RE` — `re.compile(r"^\|\s*(\d{1,3})\s*\|")`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_lint_manuscript.py`:

```python
ILLO_OK = """<!-- ILLO
id: 04-plate-01
class: plate
caption: Figure 4.1 - The filter.
alt: A cutaway of a barrel filter.
prompt: Cutaway diagram of a three-layer water filter.
-->
![Figure 4.1 - The filter.](../illustrations/04-plate-01.png)
"""


def test_valid_illo_block_passes():
    assert lint.check_illo_blocks("04-water.md", ILLO_OK) == []


def test_illo_requires_all_keys():
    text = ILLO_OK.replace("alt: A cutaway of a barrel filter.\n", "")
    errors = lint.check_illo_blocks("04-water.md", text)
    assert any("alt" in e for e in errors)


def test_illo_id_must_match_pattern():
    text = ILLO_OK.replace("04-plate-01", "04-marginalia-01")
    assert lint.check_illo_blocks("04-water.md", text) != []


def test_illo_class_must_agree_with_id_token():
    text = ILLO_OK.replace("class: plate", "class: gag")
    errors = lint.check_illo_blocks("04-water.md", text)
    assert any("class" in e for e in errors)


def test_illo_id_chapter_prefix_must_match_filename():
    errors = lint.check_illo_blocks("05-weather.md", ILLO_OK)
    assert any("prefix" in e for e in errors)


def test_illo_must_be_followed_by_its_image_link():
    text = ILLO_OK.replace("![Figure 4.1 - The filter.](../illustrations/04-plate-01.png)", "Not a link.")
    errors = lint.check_illo_blocks("04-water.md", text)
    assert any("image link" in e for e in errors)


def test_forbidden_terms_are_caught_case_insensitively():
    errors = lint.check_forbidden("04-water.md", "He drove to gas town.", ["Gas Town"])
    assert "FORBIDDEN" in errors[0]


def test_forbidden_terms_allow_clean_text():
    assert lint.check_forbidden("04-water.md", "He drove east.", ["Gas Town"]) == []


def test_cited_rules_must_exist_in_the_ledger():
    errors = lint.check_rules_cited("04-water.md", "> Rule 9: Water first.", {11})
    assert "RULE" in errors[0]
    assert "9" in errors[0]


def test_cited_rules_in_the_ledger_pass():
    assert lint.check_rules_cited("04-water.md", "> Rule 9: Water first.", {9, 11}) == []


def test_rule_ledger_is_read_from_continuity(tmp_path):
    (tmp_path / "notes").mkdir()
    (tmp_path / "notes" / "continuity.md").write_text(
        "## Rule ledger\n\n| # | Rule | Chapter |\n|---|---|---|\n| 9 | Water first. | 04 |\n| 11 | Second floor. | 02 |\n"
    )
    assert lint.read_rule_ledger(tmp_path) == {9, 11}


def test_lint_requires_an_accuracy_log_heading_per_chapter(tmp_path):
    (tmp_path / "notes").mkdir()
    (tmp_path / "manuscript").mkdir()
    (tmp_path / "notes" / "manuscript-order.txt").write_text("04-water.md\n")
    (tmp_path / "notes" / "forbidden-terms.txt").write_text("")
    (tmp_path / "notes" / "accuracy-log.md").write_text("## Chapter 01\n")
    (tmp_path / "notes" / "continuity.md").write_text("")
    (tmp_path / "manuscript" / "04-water.md").write_text(chapter())
    errors = lint.lint(tmp_path)
    assert any("ACCURACY" in e for e in errors)


def test_duplicate_illo_ids_across_chapters_are_caught(tmp_path):
    (tmp_path / "notes").mkdir()
    (tmp_path / "manuscript").mkdir()
    (tmp_path / "notes" / "manuscript-order.txt").write_text("04-water.md\n05-weather.md\n")
    (tmp_path / "notes" / "forbidden-terms.txt").write_text("")
    (tmp_path / "notes" / "accuracy-log.md").write_text("## Chapter 04\n## Chapter 05\n")
    (tmp_path / "notes" / "continuity.md").write_text("")
    (tmp_path / "manuscript" / "04-water.md").write_text(chapter() + ILLO_OK)
    (tmp_path / "manuscript" / "05-weather.md").write_text(
        chapter() + ILLO_OK.replace("04-water", "05-weather")
    )
    errors = lint.lint(tmp_path)
    assert any("DUPLICATE" in e for e in errors)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_lint_manuscript.py -q`
Expected: FAIL — `AttributeError: module 'lint_manuscript' has no attribute 'check_illo_blocks'`

- [ ] **Step 3: Add the new rules**

In `scripts/lint_manuscript.py`, change the import line and add the following. Replace the existing `lint()` function with the version below.

```python
from illo_blocks import ID_RE, parse_blocks, strip_comments

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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/ -q`
Expected: PASS, 25 passed

- [ ] **Step 5: Commit**

```bash
git add scripts/lint_manuscript.py tests/test_lint_manuscript.py
git commit -m "Add linter rules for illustration slots, forbidden terms, accuracy log, and the Rule ledger"
```

---

## Task 4: The illustration manifest collector

**Files:**
- Create: `scripts/collect_illos.py`
- Create: `tests/test_collect_illos.py`

**Interfaces:**
- Consumes: `illo_blocks.parse_blocks` from Task 1; `lint_manuscript.read_order` from Task 2.
- Produces:
  - `collect_illos.collect(root: Path) -> list[dict]` — every slot across the manuscript, sorted by id. Each dict has keys `id`, `class`, `chapter`, `source`, `caption`, `alt`, `prompt`, `path`.
  - `collect_illos.write_manifest(root: Path) -> int` — writes `notes/illustration-manifest.json` and returns the slot count.

- [ ] **Step 1: Write the failing tests**

`tests/test_collect_illos.py`:

```python
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import collect_illos


BLOCK = """<!-- ILLO
id: {id}
class: {cls}
caption: Caption text.
alt: Alt text.
prompt: Prompt text for the generator.
-->
![Caption text.](../illustrations/{id}.png)
"""


def build(tmp_path, files):
    (tmp_path / "notes").mkdir()
    (tmp_path / "manuscript").mkdir()
    (tmp_path / "notes" / "manuscript-order.txt").write_text("\n".join(files) + "\n")
    return tmp_path


def test_collects_slots_across_chapters(tmp_path):
    root = build(tmp_path, ["04-water.md", "05-weather.md"])
    (root / "manuscript" / "04-water.md").write_text(BLOCK.format(id="04-plate-01", cls="plate"))
    (root / "manuscript" / "05-weather.md").write_text(BLOCK.format(id="05-gag-01", cls="gag"))
    slots = collect_illos.collect(root)
    assert [s["id"] for s in slots] == ["04-plate-01", "05-gag-01"]


def test_slot_carries_everything_the_generator_needs(tmp_path):
    root = build(tmp_path, ["04-water.md"])
    (root / "manuscript" / "04-water.md").write_text(BLOCK.format(id="04-plate-01", cls="plate"))
    slot = collect_illos.collect(root)[0]
    assert slot["class"] == "plate"
    assert slot["chapter"] == "04"
    assert slot["source"] == "04-water.md"
    assert slot["prompt"] == "Prompt text for the generator."
    assert slot["alt"] == "Alt text."
    assert slot["path"] == "illustrations/04-plate-01.png"


def test_slots_are_sorted_by_id(tmp_path):
    root = build(tmp_path, ["04-water.md"])
    (root / "manuscript" / "04-water.md").write_text(
        BLOCK.format(id="04-plate-02", cls="plate") + BLOCK.format(id="04-gag-01", cls="gag")
    )
    assert [s["id"] for s in collect_illos.collect(root)] == ["04-gag-01", "04-plate-02"]


def test_skips_chapters_not_yet_written(tmp_path):
    root = build(tmp_path, ["04-water.md", "99-missing.md"])
    (root / "manuscript" / "04-water.md").write_text(BLOCK.format(id="04-plate-01", cls="plate"))
    assert len(collect_illos.collect(root)) == 1


def test_write_manifest_produces_valid_json(tmp_path):
    root = build(tmp_path, ["04-water.md"])
    (root / "manuscript" / "04-water.md").write_text(BLOCK.format(id="04-plate-01", cls="plate"))
    count = collect_illos.write_manifest(root)
    assert count == 1
    data = json.loads((root / "notes" / "illustration-manifest.json").read_text())
    assert data["count"] == 1
    assert data["slots"][0]["id"] == "04-plate-01"
    assert "style_guide" in data
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_collect_illos.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'collect_illos'`

- [ ] **Step 3: Write the collector**

`scripts/collect_illos.py`:

```python
"""Extract every ILLO slot in the manuscript into a batch manifest.

The manifest is the input for image generation. Nothing here generates
images; it only gathers the prompts the manuscript already carries.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from illo_blocks import parse_blocks
from lint_manuscript import read_order

MANIFEST = Path("notes") / "illustration-manifest.json"
STYLE_GUIDE = "notes/illustration-style.md"


def collect(root: Path) -> list[dict]:
    slots: list[dict] = []
    for name in read_order(root):
        path = root / "manuscript" / name
        if not path.exists():
            continue
        for block in parse_blocks(path.read_text()):
            slots.append(
                {
                    "id": block.id,
                    "class": block.cls,
                    "chapter": block.id[:2],
                    "source": name,
                    "caption": block.caption,
                    "alt": block.alt,
                    "prompt": block.prompt,
                    "path": f"illustrations/{block.id}.png",
                }
            )
    return sorted(slots, key=lambda s: s["id"])


def write_manifest(root: Path) -> int:
    slots = collect(root)
    payload = {
        "style_guide": STYLE_GUIDE,
        "note": "Prepend the fixed prompt preamble from the style guide to every prompt. Pass character and object reference sheets as reference images.",
        "count": len(slots),
        "slots": slots,
    }
    out = root / MANIFEST
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return len(slots)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    count = write_manifest(root)
    print(f"Wrote {count} slot(s) to {MANIFEST}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the full test suite**

Run: `python3 -m pytest tests/ -q`
Expected: PASS, 30 passed

- [ ] **Step 5: Verify the collector runs on the real repo**

Run: `python3 scripts/collect_illos.py`
Expected: `Wrote 0 slot(s) to notes/illustration-manifest.json.` — no chapters exist yet.

- [ ] **Step 6: Commit**

```bash
git add scripts/collect_illos.py tests/test_collect_illos.py notes/illustration-manifest.json
git commit -m "Add illustration manifest collector"
```

---

## Task 5: The style guide

**Files:**
- Create: `notes/style-guide.md`

**Interfaces:**
- Consumes: the spec's sections 1 and 3.
- Produces: the document every chapter task is written against. Defines the chapter skeleton reproduced in Task 8 and after.

- [ ] **Step 1: Write `notes/style-guide.md`**

It must contain these sections, with this content:

**1. The one rule.** The narrator is never ironic about technique. Comedy from framing, anecdote, and his sense of what is normal — never from bad information.

**2. Voice.** First person, past-weathered. Short declaratives. He never winks; no jokes are told, a worldview is reported. He addresses the reader directly and assumes they are an idiot he has decided to help anyway. Specificity over flourish: a named person and a real number beat an adjective.

**3. Tone touchstones,** as the table from the spec: Zombieland governs voice, violence, and instructiveness; Mad Max governs world only; neither contributes proper nouns. Include the line *"the narrator has seen Mad Max things and tells them in a Zombieland voice."*

**4. The dark aside.** One per chapter, maximum. One or two sentences. Dropped without comment and never revisited. Include a worked example and a counter-example:

> Good: "We buried four that winter. The ground was easier than I expected, which is its own kind of bad news."
> Bad: anything that spends a paragraph on it, or that asks the reader to feel something specific.

**5. The Rules.** Terse, deadpan, personally earned, actually correct. A Rule is compressed real advice; the comedy is in the compression. Numbering non-sequential and never reconciled. Never invent a Rule that is funny but wrong. Every Rule must be added to the `notes/continuity.md` ledger in the same commit as the chapter that cites it, or the linter fails.

**6. The chapter skeleton**, as a literal template to copy:

```markdown
# Chapter N: Title

> Rule NN: The rule, stated flat.

[Opening: ~300 words. One memory, one named person, the chapter's problem
made concrete. Ends by turning to the reader.]

## [Instruction heading]

[The real content. Numbered procedures where order matters. Tables where
tables belong. ~1,500-2,000 words total across however many headings.]

## What It Costs You

[Tradeoffs and failure modes. Where he is blunt about the price of the
technique. 150-250 words.]

## The Short Version

- [5-9 bullets, actionable without having read the chapter. May cite Rules
  by number.]
```

**7. Banned moves.** No winking at the reader. No "little did I know." No chapter that opens with a dictionary definition. No pre-Collapse brand names. No describing the Collapse's cause — he does not know and does not care, and the book is stronger for it. No second dark aside.

**8. Word budget.** 1,800–3,200 words per chapter, enforced by `scripts/lint_manuscript.py`.

- [ ] **Step 2: Verify the tooling still passes**

Run: `python3 -m pytest tests/ -q && python3 scripts/lint_manuscript.py`
Expected: tests pass; linter exits 1 with 20 `MISSING` lines and no other error type.

- [ ] **Step 3: Commit**

```bash
git add notes/style-guide.md
git commit -m "Add style guide: voice, tone touchstones, chapter skeleton"
```

---

## Task 6: The continuity bible and the Rule ledger

**Files:**
- Create: `notes/continuity.md`
- Create: `notes/accuracy-log.md`

**Interfaces:**
- Consumes: the spec's recurring-cast table; `lint_manuscript.LEDGER_ROW_RE` from Task 3, which requires ledger rows to be Markdown table rows beginning with the rule number.
- Produces: the Rule ledger that `check_rules_cited` validates against, and the accuracy log whose `## Chapter NN` headings `lint()` requires.

- [ ] **Step 1: Write `notes/continuity.md`**

**Narrator.** Unnamed throughout — people call him by role or by whatever the current group calls him. Roughly sixty when writing. Was an adult, barely, when it happened. Has belonged to eleven groups; names six in the book.

**Cast**, as a table with Name / What they are / Chapters: The Spoke (first group that took him in; competent, boring, alive; he did not appreciate it); The Ninth Hand (the blood cult, two years; he will tell you it wasn't that bad; it was that bad); Vera Ott (mechanic, taught him the machine chapters, no patience for him, dead by ch. 16); The Bell Country (the settlement he founded and lost; ch. 15 is his own cautionary material); Mother Furnace (a god he invented by committee in an afternoon, for morale; still worshipped; six-spoke iron shape); Ais (the apprentice he is writing for; named rarely; ch. 20 is addressed to her).

**Timeline.** Year 0 the Collapse. Y0–1 alone, then the Spoke. Y3–5 the Ninth Hand. Y6 meets Vera. Y9–14 the Bell Country, and Mother Furnace is invented in Y11. Y14 the Bell Country ends. Y15+ itinerant, teaching. Y40 he writes this. Two generations later the manuscript is found.

**Places.** Invent as needed; record every one here on first use so no settlement gets two names.

**Rule ledger.** A Markdown table with columns `| # | Rule | Chapter |`, seeded with the rules below. **Every row must begin with the number so the linter can read it.** Add a row in the same commit as the chapter that first cites the Rule.

| # | Rule | Chapter |
|---|------|---------|
| 4 | Count before you move. | 01 |
| 9 | Water first. Always. | 04 |
| 11 | The second floor is not safer. It is only harder to leave. | 02 |
| 80 | *Reserved. Spent in chapter 20. Do not cite before then.* | 20 |

Rule 80 is the reserved final rule — the soft rule that outranks the hard ones. Its text is written in Task 27 and not before.

- [ ] **Step 2: Write `notes/accuracy-log.md`**

A header explaining the file's job — the real-world basis for every load-bearing claim, auditable separately from the voice — followed by one `## Chapter NN` heading for each of the twenty chapters, `## Chapter 01` through `## Chapter 20`. Each heading starts with the single line `_No entries yet._`, replaced as chapters are written.

Entry format, documented at the top of the file:

```markdown
- **Claim as stated in the chapter.** Basis: [source and what it says]. Confidence: high | conservative-choice | vague-on-purpose.
```

- [ ] **Step 3: Verify the ledger and log parse**

Run:
```bash
python3 -c "
import sys; sys.path.insert(0, 'scripts')
from pathlib import Path
import lint_manuscript as l
print('ledger:', sorted(l.read_rule_ledger(Path('.'))))
print('logged chapters:', len(l.read_accuracy_chapters(Path('.'))))
"
```
Expected: `ledger: [4, 9, 11, 80]` and `logged chapters: 20`

- [ ] **Step 4: Confirm the linter's only complaints are missing chapters**

Run: `python3 scripts/lint_manuscript.py`
Expected: exit 1, exactly 20 lines, all `MISSING`. No `ACCURACY` errors — the log now covers every chapter.

- [ ] **Step 5: Commit**

```bash
git add notes/continuity.md notes/accuracy-log.md
git commit -m "Add continuity bible, Rule ledger, and accuracy log skeleton"
```

---

## Task 7: The illustration style guide

**Files:**
- Create: `notes/illustration-style.md`

**Interfaces:**
- Consumes: the spec's section 5.
- Produces: the fixed prompt preamble that `collect_illos.write_manifest` tells the generator to prepend, and the character sheet list that becomes the first generation run.

- [ ] **Step 1: Write `notes/illustration-style.md`**

**1. The fixed prompt preamble.** A verbatim block, prepended to every generation without exception:

> Two-ink civil-defense manual illustration. Flat black line art plus a single rust-orange spot color, printed on cream paper with visible paper grain and slight ink misregistration. Heavy confident outlines, no gradients, no rendered lighting, no texture shading. Cartoonish rubbery figures with simple bean-shaped bodies, oversized hands, small heads, expressive postures. 1950s government pamphlet layout sensibility. Flat, graphic, legible at small size.

**2. Palette.** Ink black `#1A1A1A`, rust orange `#C25B2A`, paper cream `#EFE6D4`. Three colors only. The orange carries emphasis and nothing else.

**3. The do-not list.** No gradients. No rendered or cinematic lighting. No photoreal faces. No text in the image beyond callout numerals. No more than three colors. No modern logos or brand marks. No gore. No depiction of weapons manufacture.

**4. The two classes.**

*Plates* teach. Numbered callouts keyed to the caption, labeled parts, correct technique. A plate is reviewed against `notes/accuracy-log.md` exactly as prose is — an inaccurate plate is worse than no plate. Composition: single subject, generous white space, callout numerals in orange circles.

*Gags* are marginalia. Small, loose, placed in the margin of the argument rather than the center. Never load-bearing — a reader who skips every gag loses nothing but fun.

**5. Character and object sheets.** The first generation run produces reference sheets, before any chapter illustration. Every subsequent generation passes the relevant sheet in as a reference image. Each entry fixes the silhouette, since silhouette is what survives style drift:

- **The narrator** — older man, long coat cut from a tarp, flat cap, one bad knee. Drawn from behind or in three-quarter profile wherever possible; his face is never the subject.
- **Vera Ott** — stocky, overalls, welding mask pushed up on her forehead so her face is framed by it. Always holding a tool, always mid-sentence.
- **Ais** — teenager, too-large coat, close-cropped hair, carries a satchel of papers.
- **Mother Furnace** — never a person. Always the same six-spoke iron wheel with a square furnace door at the hub, rendered as an icon.
- **The Ninth Hand's mark** — a nine-fingered handprint, orange, stamped not drawn.
- **The Spoke's mark** — a wheel hub with five spokes and one missing.
- **The go-bag** — the same bag in every appearance: canvas, two buckles, a patch on the lower left corner.

**6. Slot block format.** The authoritative `ILLO` block syntax, with a worked example, and the note that `scripts/lint_manuscript.py` enforces it: `id` must look like `NN-plate-NN` or `NN-gag-NN`, `class` must match the id's token, the chapter prefix must match the filename, and the block must be immediately followed by its image link.

**7. Budget.** ~3 slots per chapter, roughly 1 plate and 2 gags. ~60 total.

**8. Generation workflow,** for when nano banana is connected: regenerate the manifest with `python3 scripts/collect_illos.py`; generate the character and object sheets first; then batch the manifest, preamble plus slot prompt plus relevant reference sheets; write each result to `illustrations/<id>.png`, at which point every image link in the manuscript resolves with no edit to the prose. Review plates against the accuracy log before accepting them.

- [ ] **Step 2: Commit**

```bash
git add notes/illustration-style.md
git commit -m "Add illustration style guide: preamble, palette, character sheets"
```

---

## Task 8: Front matter

**Files:**
- Create: `manuscript/00-front-matter.md`

**Interfaces:**
- Consumes: `notes/style-guide.md`, `notes/continuity.md`.
- Produces: the book's opening. Exempt from the chapter apparatus rules — the linter does not check `00-`.

- [ ] **Step 1: Write `manuscript/00-front-matter.md`**

Three parts, in this order.

**1. Author's note — real voice, not in character.** Four plain lines, no styling, no jokes. It says: this book is a comedy; the survival techniques in it are accurate to the best of our knowledge as of writing and are drawn from published emergency guidance; it is not a substitute for training; nobody should learn medicine from a novel. This page is non-negotiable and never written in the narrator's voice.

**2. Editor's preface — in fiction, ~400 words.** Written two generations later by someone who has never seen a working lightbulb and does not entirely believe in them. They explain: where the pages were found, the water damage, which chapters are missing or partial, and that they have left the author's spelling alone. They are reverent about the wrong things — fascinated by his description of a refrigerator, bored by the chapter on bleeding control. One line establishes that the Rules are quoted by people who have never read the book. Signed with an initial and a place name.

**3. Contents.** The five Parts with their subtitles and all twenty chapter titles, as a nested list. Part subtitles: The First Hour — *what kills you before you have a plan*; The First Week; The First Year; The Long After; What Comes After You.

- [ ] **Step 2: Verify the linter ignores front matter**

Run: `python3 scripts/lint_manuscript.py`
Expected: exit 1 with exactly 20 `MISSING` lines. No errors mentioning `00-front-matter.md`.

- [ ] **Step 3: Commit**

```bash
git add manuscript/00-front-matter.md
git commit -m "Add front matter: author's note, editor's preface, contents"
```

---

## Chapter task template

Tasks 9–28 are the twenty chapters. **Every chapter task has the same five steps**, listed once here and referenced by each task. Each task below supplies only what is specific to that chapter: its brief, its Rules, its accuracy entries, and its illustration slots.

For chapter `NN-slug.md`:

- [ ] **Step 1: Confirm the red state**

Run: `python3 scripts/lint_manuscript.py 2>&1 | grep NN-slug.md`
Expected: `NN-slug.md: MISSING: listed in manuscript-order.txt but not written yet`

- [ ] **Step 2: Write the chapter**

Copy the skeleton from `notes/style-guide.md` section 6. Follow the brief in this task. Re-read `notes/style-guide.md` sections 1, 4, and 7 before starting and the brief's banned-move notes before finishing. Place the illustration slots where the brief specifies, each with a full `ILLO` block and its image link.

- [ ] **Step 3: Update the ledger and the log**

Add any newly cited Rule as a row in the `notes/continuity.md` ledger. Replace `_No entries yet._` under `## Chapter NN` in `notes/accuracy-log.md` with one entry per load-bearing claim, in the documented format. Record any newly invented place or person in the continuity bible.

- [ ] **Step 4: Verify green**

Run: `python3 scripts/lint_manuscript.py 2>&1 | grep NN-slug.md; python3 scripts/collect_illos.py`
Expected: no output from `grep` — the chapter is clean. The collector prints an increased slot count.

- [ ] **Step 5: Commit**

```bash
git add manuscript/NN-slug.md notes/continuity.md notes/accuracy-log.md notes/illustration-manifest.json
git commit -m "Write chapter NN: <title>"
```

---

## Task 9: Chapter 1 — Triage: Decide What You Are

**Files:**
- Create: `manuscript/01-triage.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The book's first chapter has one job: teach the reader to order their own problems instead of solving whichever one is loudest. Open with the first hour — he spent it looking for his glasses. Cites that as the stupidest hour of his life and the reason he is qualified to write this.

Instruction: the rule of threes as a triage tool (roughly three minutes without air, three hours without shelter in genuinely hostile cold or heat, three days without water, three weeks without food) — presented as *the order to think in*, with the explicit caveat that the numbers are a mnemonic and not a guarantee. Then panic as a cause of death: what it actually does to decision-making, and the specific countermeasure of doing one small ordered physical task. Then the three questions that order everything after: Am I bleeding? Can I breathe where I am standing? Does anyone know where I am? Close on *Rule 4: Count before you move* — which is both a joke about his glasses and the actual technique.

**Rules.** Introduces **Rule 4: Count before you move.** (already in the seeded ledger).

**Accuracy entries.** The rule-of-threes mnemonic, flagged as a mnemonic with the real caveats. Panic/acute stress effects on decision-making. The "do one ordered task" countermeasure.

**Illustration slots.** `01-plate-01` — the rule of threes as a four-step orange staircase, each tread labeled with its interval. `01-gag-01` — a man on his knees in debris patting the floor for his glasses, apocalypse visible and ignored through the window behind him. `01-gag-02` — the three questions as a tiny flowchart, drawn on the back of an envelope.

**Banned moves for this chapter.** Do not describe the Collapse's cause. Do not open on the word "survival."

---

## Task 10: Chapter 2 — Run or Dig In

**Files:**
- Create: `manuscript/02-run-or-dig-in.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The decision everyone gets wrong in both directions. Open with the Spoke's rule about it, and the fact that the Spoke was boring and alive while the clever people were neither.

Instruction: the real shelter-in-place vs. evacuate decision — what makes staying correct (structure sound, water on hand, the hazard is outside and passing), what makes leaving correct (structure compromised, hazard is where you are and worsening, no water), and the trap of leaving late, which is how most people die of this decision. Then the go-bag: the bag you should already own, built around water, light, warmth, documents, medication, and a knife, with the honest note that everyone's first bag is too heavy and the fix is carrying it up a flight of stairs once. Then route choice: roads are fast and watched, water courses navigate themselves, and the second floor is not safer.

**Rules.** Cites **Rule 11: The second floor is not safer. It is only harder to leave.** (seeded). Introduces **Rule 23: Pack the bag for the stairs, not for the road.**

**Accuracy entries.** Shelter-in-place vs. evacuation decision factors. Go-bag contents and the water-weight tradeoff. Why leaving late is the dominant failure mode.

**Illustration slots.** `02-plate-01` — the go-bag cutaway, contents numbered with orange callouts, the same canvas bag from the style sheet. `02-gag-01` — two identical men, one labeled TOO EARLY sitting bored on a hill, one labeled TOO LATE as a pair of boots in a doorway. `02-gag-02` — the first bag, absurdly overpacked, with a cast-iron pan lashed to it.

---

## Task 11: Chapter 3 — The Body Is Your First Vehicle

**Files:**
- Create: `manuscript/03-body.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The most load-bearing chapter in the book for accuracy. The narrator is noticeably more careful here than anywhere else, and says so: this is the one chapter he made someone else check.

Instruction, in strict priority order: severe bleeding first — direct pressure, hard and continuous, with the real detail that pressure means one spot and both hands and minutes, not dabbing; wound packing; tourniquet placement high and tight above the wound, not over a joint, tightened until bleeding stops, time noted, never loosened by the person who applied it. Then airway and breathing. Then shock — recognition and positioning, keep warm, no food or drink. Then fractures — splint in the position found, immobilize the joints above and below, check circulation past the splint. Then the honest list of what he cannot fix and neither can you: internal bleeding, head injuries that worsen, anything abdominal. He is plain that the correct answer to most of those used to be a hospital and is now company.

**Rules.** Introduces **Rule 7: Pressure is a place, not a motion.**

**Accuracy entries.** One per technique above, each with its published basis and a confidence marker. Tourniquet guidance and the never-loosen point get their own entries. The "what cannot be fixed" list gets an entry confirming it is accurately scoped.

**Illustration slots.** `03-plate-01` — direct pressure and wound packing, two panels, numbered callouts, hands only, no gore, no blood depicted as color. `03-plate-02` — tourniquet placement on a limb diagram, with the orange callout for the time-written-down step. `03-gag-01` — the narrator's own list of things he has splinted with, including a road sign and, labeled regrettable, a guitar neck.

**Banned moves for this chapter.** No gore in prose or plate. No joke lands inside a procedure — the dark aside, if used, goes in the closing section, not the instruction.

---

> ## REVIEW CHECKPOINT — end of Part I
>
> Stop. Do not begin Task 12.
>
> Run `python3 -m pytest tests/ -q`, `python3 scripts/lint_manuscript.py`, and `python3 scripts/collect_illos.py`, then report the chapter word counts.
>
> Ask the user to read chapters 1–3 and confirm: is the narrator's register right? Is the comedy-to-instruction ratio right? Is the dark aside landing as a trapdoor rather than a tone shift? Are the chapters too dense or too thin?
>
> Apply any corrections to all three chapters **and to `notes/style-guide.md`** before continuing, so the correction propagates instead of being re-litigated at chapter 12.

---

## Task 12: Chapter 4 — Water, and the Lies People Tell About It

**Files:**
- Create: `manuscript/04-water.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open on the Ninth Hand's water ceremony, which was theater, and the fact that the theater was load-bearing anyway — the first quiet foreshadowing of Part V. Then he gets practical and slightly annoyed.

Instruction: quantity first — roughly one gallon per person per day for drinking and basic hygiene, more in heat or exertion, and the note that rationing water is a worse idea than people think because dehydration degrades the judgment you need to find more. Sourcing, ranked by trouble: stored and tanked water, rain catchment, flowing surface water, standing water, and the ones not worth it. Then treatment, carefully distinguished: filtration removes particulates and some organisms but is not disinfection; boiling is the most reliable method available (a rolling boil, one minute, three minutes at high altitude); chemical treatment with unscented household bleach at the published ratio, mixed, stood for the published time, and the clear statement that cloudy water must be filtered or settled first and the dose changes. The lies in the title: that running water is safe, that clear water is clean, that you can taste the difference, and that a filter straw is a water plan.

**Rules.** Cites **Rule 9: Water first. Always.** (seeded). Introduces **Rule 28: Clear is not clean.**

**Accuracy entries.** Daily water quantity. Boil times including altitude. Bleach concentration, dose, contact time, and the cloudy-water caveat — this entry must name its source precisely and be marked conservative-choice. Filtration vs. disinfection distinction. The rationing point.

**Illustration slots.** `04-plate-01` — the three-stage barrel filter in cutaway, layers numbered, captioned so that the stage everyone skips is the one the caption names. `04-plate-02` — a treatment decision diagram: clear vs. cloudy, into boil vs. filter-then-treat. `04-gag-01` — the Ninth Hand's water ceremony, nine-fingered handprints on the cistern, everyone extremely solemn about a bucket.

---

## Task 13: Chapter 5 — Two Ways Weather Kills You

**Files:**
- Create: `manuscript/05-weather.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open with his conviction, held for two years, that cold kills by being cold. It kills by being wet, and he learned that the hard way at about four degrees above freezing, which is the temperature at which people who think they understand hypothermia get it.

Instruction: cold first — wet and wind as the real multipliers, the mechanics of insulation (loft, layers, and the ground stealing more heat than the air), recognition of hypothermia including the fumbling and the mood change that precedes the shivering stopping, and rewarming done gradually with the caveats about alcohol and about rubbing. Then heat — the distinction between heat exhaustion and heat stroke, which is the one to actually memorize, because one is rest and fluids and shade and the other is an emergency defined by altered mental state; active cooling; working the cool hours and sleeping the hot ones. Then shelter as a heat problem rather than an architecture problem: small, insulated from the ground, ventilated, and the near-universal beginner error of building something impressively large and unheatable. Then fire: fuel laddering, a real reason to prefer a small fire, and carbon monoxide, which he introduces by saying he has lost more people to enclosed fires than to the cold they were escaping.

**Rules.** Introduces **Rule 16: Wet is colder than cold.** and **Rule 34: Build small. Heat is the rent.**

**Accuracy entries.** Hypothermia recognition sequence and rewarming cautions. Ground conduction. Heat exhaustion vs. heat stroke differentiation and the altered-mental-state red flag. Active cooling. Carbon monoxide risk from enclosed combustion.

**Illustration slots.** `05-plate-01` — the layering diagram, three layers numbered, with the ground-insulation callout emphasized in orange. `05-plate-02` — heat exhaustion vs. heat stroke as a two-column comparison, the altered-mental-state row flagged. `05-gag-01` — a beautifully built, enormous, freezing shelter, with the narrator looking at it with visible regret.

---

## Task 14: Chapter 6 — Food Matters Later Than You Think

**Files:**
- Create: `manuscript/06-food.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open with the man who starved to death with four hundred pounds of dried beans, because panic is not a calorie and he never learned to cook them. Then the central, deliberately deflating point: in the first week food is a morale problem, not a survival problem, and treating it as the emergency is how people drown while looking for lunch.

Instruction: calorie math done honestly — a sedentary adult's maintenance versus what hard physical labor actually costs, and the consequence that a working survivor needs far more than a hiding one. What stores and what does not: the real shelf behavior of grains, legumes, fats (the first thing to go rancid and the thing you will crave most), salt as the most valuable thing in a pantry, and canned goods including the specific warnings — bulging, leaking, and seams — that mean do not open it. Then foraging, handled with deliberate skepticism: the calorie return on wild plants is poor, misidentification is a real and occasionally fatal risk, and the only honest advice is to learn three local plants cold from someone who knows them rather than twenty from a book. Then the chapter's genuine skill, cooking dried legumes and grains with scarce fuel: soaking, a lid, and the insulated-pot trick, which turns fuel into time.

**Rules.** Introduces **Rule 19: Salt is money.** and **Rule 42: Learn three plants completely before you learn twenty badly.**

**Accuracy entries.** Maintenance vs. labor calorie ranges. Shelf-stability ordering of staples and fat rancidity. Canned-goods spoilage warning signs. The foraging calorie-return and misidentification caution. Fuel-efficient legume cooking.

**Illustration slots.** `06-plate-01` — the insulated-pot method in four numbered panels. `06-plate-02` — a can with the three warning signs labeled in orange, captioned flatly. `06-gag-01` — the bean man's pantry, magnificent and untouched, one pot on the floor.

---

## Task 15: Chapter 7 — The First People You Meet

**Files:**
- Create: `manuscript/07-first-people.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The hinge chapter: the book pivots from things to people and never fully goes back. Open with the first stranger he met after the Spoke, who he nearly killed out of pure fright, and who later taught him to read a settlement. He does not name her and says why: she asked him not to put her in a book, and that is the kind of promise he still keeps.

Instruction: reading a group from outside before you approach — what the condition of their water, their children, their animals, and their fences tells you, and the specific tell that a place with no visible children and plenty of food is a place to walk past. Approach technique: visible hands, visible hunger, approach in daylight, and the difference between being unarmed and being harmless. Trade as the universal first conversation, with the real guidance that the first trade should be small, immediately resolved, and slightly in their favor. Then walking away: the signs that a group is not safe to join, and the single most useful thing in the chapter — that leaving is a skill, requires knowing your route out before you go in, and gets harder every day you stay. He notes he knew every one of these signs at the Ninth Hand and joined anyway. That is the chapter's dark aside and the setup for chapter 15.

**Rules.** Introduces **Rule 31: Know the way out before you go in.** and **Rule 12: Small first trade. Resolve it the same day.**

**Accuracy entries.** Settlement condition indicators as genuine welfare signals. De-escalation and approach practice. Small-stakes first exchange as a trust-building mechanism.

**Illustration slots.** `07-plate-01` — "reading a settlement from the ridge," a single wide scene with six orange numbered callouts keyed to the caption. `07-gag-01` — the correct approach posture and three incorrect ones, labeled, the last one captioned simply NO. `07-gag-02` — the Ninth Hand's gate, inviting, well-maintained, with nine-fingered handprints on it.

---

> ## REVIEW CHECKPOINT — end of Part II
>
> Stop. Do not begin Task 16.
>
> Run the full tooling pass and report word counts for chapters 1–7 plus the running total.
>
> Ask the user to read chapters 4–7 and confirm: is the Rules device earning its place or becoming a tic? Is the Ninth Hand thread building properly toward chapter 15? Is the accuracy log honest and specific enough to audit?
>
> Apply corrections to the written chapters and the style guide before continuing.

---

## Task 16: Chapter 8 — Gear That Earns Its Weight

**Files:**
- Create: `manuscript/08-gear.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open on the pre-Collapse prepper's cache he found in year three: eleven thousand dollars of equipment, none of it maintained, the batteries dead in their housings and the canvas rotted, and a laminated inventory list. He kept the list. It was the only useful thing in there.

Instruction: the single organizing principle — gear is a loan against your future strength, and every item must pay rent in grams. The categories that always earn it: a container, a cutting edge, cordage, a means of making fire, light, and a way to carry water. Redundancy done properly, which means two different methods rather than two identical objects. Maintenance as the actual skill: edges, rust, canvas, rubber, and the fact that nearly all abandoned gear failed from neglect rather than use. Repairability as a purchase criterion. Then the honest section on what he carries now, which is embarrassingly little, and why that took twenty years to learn.

**Rules.** Introduces **Rule 6: Two methods, not two objects.** and **Rule 55: Gear you do not maintain is gear you do not have.**

**Accuracy entries.** Degradation modes and realistic timelines for batteries, rubber, canvas, and fuel. Edge maintenance and rust prevention. The redundancy principle as a real reliability practice.

**Illustration slots.** `08-plate-01` — the six categories as labeled icons, one per category, orange numerals. `08-gag-01` — the prepper's cache, magnificent and ruined, laminated list glowing with importance in orange. `08-gag-02` — the narrator's actual current kit, laid out flat, pathetically small, captioned with quiet pride.

---

## Task 17: Chapter 9 — Scavenging Is a Profession

**Files:**
- Create: `manuscript/09-scavenging.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open with the observation that amateurs loot the front of the store and professionals go to the stockroom, the maintenance closet, and the roof. The difference is not courage, it is method, and method is teachable.

Instruction: search as a systematic sweep rather than a treasure hunt — one direction, one room at a time, high and low, marking what has been cleared so you do not re-search and so the next person knows. Structural safety before value: what makes a building not worth entering, floor and stair assessment, and the rule that nothing inside is worth being trapped inside with. The places that are reliably unsearched: utility and janitorial spaces, vehicle trunks, the backs of appliances, pharmacy stockrooms rather than shelves, and office first-aid cabinets. What is actually valuable in year three versus year one — fasteners, fuel containers, intact rubber hose, medical supplies, salt, needles and thread, and the fact that nobody takes the needles. Then the ethics he actually holds, offered without preaching: he takes from the dead and not from the living, he does not strip a place a family is still using, and he leaves water.

**Rules.** Introduces **Rule 21: Stockroom, not showroom.** and **Rule 47: Mark what you clear.**

**Accuracy entries.** Structural assessment indicators for unsafe buildings. Systematic search methodology. Realistic salvage-value ordering.

**Illustration slots.** `09-plate-01` — the sweep pattern through a floor plan, an orange dashed route with numbered stops and the clearing mark shown. `09-plate-02` — the clearing mark itself, drawn large, with its three variants labeled. `09-gag-01` — two scavengers, one wrestling a television, one quietly pocketing a box of needles.

---

## Task 18: Chapter 10 — The Machine

**Files:**
- Create: `manuscript/10-machine.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Vera Ott's chapter, and the only one where the narrator is clearly out of his depth and knows it. Open with her assessment of him, which was accurate and unkind. Her voice runs through the chapter as interruptions he is still hearing thirty years later.

Instruction: fuel first, because fuel is the whole problem — gasoline degrades over months and is the least durable thing in the fuel chain, diesel keeps longer but has its own problems, storage wants full, sealed, cool and dark containers, and the real safety content on vapor, static, and never doing any of it indoors. Then engine triage as a diagnostic order rather than a repair manual: fuel, spark, air, compression, and the discipline of checking the stupid thing first because it is usually the stupid thing. Tires, which are the actual limiting factor on a vehicle's life and cannot be manufactured by anyone the reader will ever meet. Then the chapter's honest spine, which is Vera's: most vehicles are not repairable by you, the correct relationship to a machine is maintenance rather than heroics, and a bicycle you can fix will outlast a truck you cannot. The dark aside belongs to how she died, in one line, not in this chapter's instruction.

**Rules.** Introduces **Rule 38: Check the stupid thing first.** and **Rule 64: A bicycle you can fix beats a truck you cannot.**

**Accuracy entries.** Gasoline and diesel shelf life and storage conditions. Fuel-handling safety: vapor, static, ventilation. The fuel/spark/air/compression diagnostic order. Tire degradation as the binding constraint.

**Illustration slots.** `10-plate-01` — the fuel storage diagram, correct and incorrect containers side by side, the orange callout on ventilation. `10-plate-02` — the four-step triage order as a flowchart, "check the stupid thing first" as step zero. `10-gag-01` — Vera Ott, welding mask up, mid-sentence, pointing at something off-panel with a wrench.

**Banned moves for this chapter.** No weapons content. Do not let the fuel section drift into anything incendiary — it is a storage-and-safety section and stays one.

---

## Task 19: Chapter 11 — Voices Across the Waste

**Files:**
- Create: `manuscript/11-voices.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open with the four months he spent believing he was the last person alive, which ended when he heard a woman reciting a shopping list over a radio for the company of saying it. He says that is still the most beautiful thing he has ever heard. Sincerity arrives suddenly here and is not apologized for.

Instruction: the cheap methods first, because they work — a message left where it will be found, the convention of a dead drop and a mark, and a schedule, which is the single highest-value idea in the chapter: two people who agree to check the same place on the same day of the week have solved most of their communication problem without any equipment. Then signaling: contrast, movement, and regularity as the three things that read as human at distance; why three of anything signals distress; why signals must be pointed at where people actually are. Then radio, honestly scoped: line of sight for the handhelds most people will find, antenna height mattering more than power, batteries as the real constraint, listening schedules, and the strong advice to listen far more than you transmit. Then navigation: maps as consumables, keeping a written route log, pacing, and the honest point that getting unlost is mostly a matter of having written down where you were.

**Rules.** Introduces **Rule 14: Agree on a schedule and a place. That is a radio you do not have to carry.** and **Rule 72: Listen longer than you transmit.**

**Accuracy entries.** Rule-of-three distress signaling. Contrast/movement/regularity as detection factors. VHF/UHF line-of-sight behavior and antenna height vs. power. Dead reckoning and route logging.

**Illustration slots.** `11-plate-01` — the dead drop and its mark, cutaway, numbered. `11-plate-02` — antenna height versus power, two figures on a hill and in a valley, orange arcs showing range. `11-gag-01` — the shopping list, hand-lettered on a scrap, treated as a holy relic in a frame.

---

## Task 20: Chapter 12 — Rot, Teeth, and Other Slow Deaths

**Files:**
- Create: `manuscript/12-rot.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The chapter he says no one wants and everyone needs: nobody plans for the apocalypse by learning to dig a latrine properly, and more of his friends died of this chapter than of any other.

Instruction: sanitation as the single highest-return survival practice there is — latrine siting relative to water and to living space, depth, covering, and the handwashing that is the actual intervention. Then water-borne and faecal-oral disease in plain terms, and the honest arithmetic that diarrhoeal illness kills far more people in a collapse than violence does, together with the one countermeasure anyone can do: oral rehydration, with the published salt-and-sugar ratio stated conservatively and the note that clean water matters more than the recipe. Then wound care over time: cleaning, irrigation, keeping it covered, the specific signs of infection worth acting on, and the limits of what topical care achieves. Then teeth, which get real space because nothing else in the book is as certain to happen to the reader: the unglamorous prevention that actually works, what an abscess is and why it is an emergency rather than an inconvenience, and his flat refusal to explain amateur extraction. Closes on hygiene as morale, which is the bridge to chapter 16.

**Rules.** Introduces **Rule 2: Wash your hands. I am serious. This is Rule 2.** and **Rule 29: Downhill and far from the water.**

**Accuracy entries.** Latrine siting distances and depth. Handwashing as the primary intervention. Diarrhoeal disease burden. Oral rehydration solution ratio — named source, marked conservative-choice, with the clean-water caveat. Infection warning signs. Dental abscess as a genuine emergency.

**Illustration slots.** `12-plate-01` — latrine siting, cross-section of slope, water, and dwelling, with orange distance callouts. `12-plate-02` — the oral rehydration recipe as a measured diagram, deliberately plain. `12-gag-01` — Rule 2 rendered as a devotional poster, far too ornate, hung crooked.

---

> ## REVIEW CHECKPOINT — end of Part III
>
> Stop. Do not begin Task 21.
>
> Run the full tooling pass. Report word counts for chapters 1–12, the running total, and the manifest slot count.
>
> Ask the user to read chapters 8–12 and confirm: is Vera Ott working as a second voice? Is the book's halfway point still funny, or has the practical density crowded the comedy out? Is the Rule corpus coherent — do any two Rules contradict each other?
>
> Also verify the midpoint projection: at twelve chapters the total should be tracking toward 45k–55k. If it is tracking high, decide now whether Part IV and V chapters run shorter, rather than discovering it at chapter 20.

---

## Task 21: Chapter 13 — Growing Things, Keeping Things

**Files:**
- Create: `manuscript/13-growing.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The chapter where the book's timeline turns: everything before this assumed you were passing through, and this one assumes you are staying. Open with the Bell Country's first garden, which failed completely, and the second, which did not, and the difference between them, which was water and patience rather than knowledge.

Instruction: water capture before planting, because catchment area and storage, not soil, is what caps a garden — roof area, first-flush diversion, covered storage, and the mosquito problem. Soil as something built rather than found: compost, the nitrogen cycle in plain language, and why the first year's yield is a lie in both directions. Crop choice by calorie density and storability rather than by what is pleasant, which means roots, legumes, and squash before salad. Seed saving, with the genuinely important point about hybrid versus open-pollinated seed, since a reader who saves seed from the wrong packet gets one good year and then nothing. Then preservation, the chapter's most useful half: drying as the most forgiving method, salting, and fermentation, with the real safety lines drawn clearly — what is low-risk (drying, high-salt ferments) versus what requires equipment and precision he tells the reader not to improvise, naming home canning of low-acid foods specifically as the thing not to guess at.

**Rules.** Introduces **Rule 51: The roof is a field.** and **Rule 58: Plant calories, not salad.**

**Accuracy entries.** Rainwater catchment yield and first-flush diversion. Covered storage and vector control. Compost and nitrogen basics. Open-pollinated vs. hybrid seed saving. Drying, salting, and fermentation safety, with an explicit entry on botulism risk in improvised low-acid canning, marked conservative-choice.

**Illustration slots.** `13-plate-01` — the catchment system, roof to first-flush to covered cistern, numbered. `13-plate-02` — three preservation methods in three columns, with the fourth column crossed out in orange and labeled NOT WITHOUT EQUIPMENT. `13-gag-01` — the Bell Country's first garden, immaculate rows, entirely dead, a hand-painted sign reading HOPE.

---

## Task 22: Chapter 14 — The Economy of Nothing

**Files:**
- Create: `manuscript/14-economy.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Open with the man who tried to introduce currency to the Bell Country, backed by nothing but his own confidence, and who was both completely wrong and the most useful idiot they had, because the argument he started taught everyone what they actually valued.

Instruction: what makes a thing money — durability, divisibility, portability, and agreement — and the observation that salt, ammunition, fuel, and medicine all become money because all four qualify, which he notes without enthusiasm. Barter mechanics done properly: never name the first number on something you need, the difference between price and value, bundling, and why trading away tools is almost always a mistake even at a good price. Debt and favors as the real economy of small groups, and the uncomfortable fact that favors are a better store of value than any object, provided the group survives. Then the practical fraud section, which is the chapter's best material: diluted and relabelled goods, weighted scales, the short count, the too-good trade as a reliable marker of either ignorance or a setup, and his list of the specific tells. Closes on reputation as the actual currency — slow to earn, impossible to repair, and the reason he still will not trade in one particular valley.

**Rules.** Introduces **Rule 26: Never name the first number.** and **Rule 68: Reputation spends everywhere and cannot be minted.**

**Accuracy entries.** Properties of money as a real economic framework. Barter negotiation dynamics. Reciprocal-favor economies as documented practice in small groups. Common fraud techniques as recognition material, framed defensively.

**Illustration slots.** `14-plate-01` — the four properties of money as four labeled panels, with salt shown satisfying all four. `14-plate-02` — three fraud tells drawn plainly: the weighted scale, the diluted jar, the short count. `14-gag-01` — the currency man's banknote, hand-drawn, self-portrait on it, denomination ONE.

---

## Task 23: Chapter 15 — How Groups Decide Things

**Files:**
- Create: `manuscript/15-groups.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The book's hardest chapter and its most honest. He led the Bell Country and he lost it, and this chapter is the autopsy. He is specific that the failure was structural rather than villainous, which is what makes it worth reading: nobody in the Bell Country was a bad person, and it still came apart.

Instruction: group size and the real thresholds at which informal consensus stops working, and why a group that has outgrown the kitchen table needs structure whether or not anyone wants it. Decision mechanisms compared honestly — consensus, voting, a council, and a single decider — with the conditions under which each works and the specific failure each produces. Rationing as a legitimacy problem rather than a math problem, with the central point that a visibly fair process beats a cleverly optimal one every time. Conflict and exile, which he treats as a mechanism that must exist and must be bounded, written down in advance, and never decided by the person who was wronged. Then the chapter's spine, the failure modes, drawn from the Ninth Hand and from his own tenure and framed entirely as **things to recognize and resist**: information held by one person; a leader exempt from the rules; a group whose membership cost keeps rising; the reframing of doubt as disloyalty; and the one he is most ashamed of, which is a decision structure he quietly stopped using because it kept telling him no. He names it plainly. He does not explain how to do any of it to someone else.

**Rules.** Introduces **Rule 44: Write the exile rule before you need it.** and **Rule 77: A leader exempt from a rule has repealed it.**

**Accuracy entries.** Group-size thresholds for informal coordination. Procedural-fairness research on legitimacy versus outcome. Decision-mechanism tradeoffs. Coercive-control warning signs, cited as recognition and exit material from established sources.

**Illustration slots.** `15-plate-01` — the four decision mechanisms as a comparison table, each with its characteristic failure in orange. `15-plate-02` — the five warning signs as five icons, captioned RECOGNIZE, NOT BUILD. `15-gag-01` — the Bell Country's council table, nine chairs, one visibly nicer than the others, which is the whole chapter in one drawing.

**Banned moves for this chapter.** No operationalized manipulation technique — every coercion item is framed as recognition and exit. No villain. The Ninth Hand's leader is never described as charismatic in a way that reads as admiring.

---

## Task 24: Chapter 16 — Grief, Boredom, and Morale

**Files:**
- Create: `manuscript/16-grief.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Vera Ott dies in this chapter, in one line, and the chapter is not about her death. It is about the eight months afterward, which is the part nobody prepares for. The two killers of the title are the ones no prepper stocks for: grief, which takes people quickly, and boredom, which takes them slowly and is far more common.

Instruction: grief handled plainly and without instruction — what it does to judgment and to physical safety, the fact that the dangerous period is weeks after rather than days, and the only real countermeasure he knows, which is other people noticing and the specific practice of assigning a grieving person a small daily duty that someone else depends on. Then boredom treated as the serious hazard it is: understimulation driving risk-taking, conflict, and drift, and the observation that more groups dissolved from nothing to do than from any threat. Morale as infrastructure — meals eaten together, work that visibly finishes, music, a day off that is actually off, and projects with an end. Sleep and routine as the cheapest interventions available. Then the hinge of the whole book, stated here for the first time outright: the things that look like frivolity are load-bearing, and the chapters that follow are about building them deliberately. He admits he thought this was nonsense until the Bell Country's third winter, when the only thing that held was a weekly dinner nobody could explain the point of.

**Rules.** Introduces **Rule 61: A day off is maintenance.** and **Rule 36: Give the grieving a duty someone depends on.**

**Accuracy entries.** Bereavement and risk/judgment effects, with the delayed-onset point. Understimulation and risk-taking. Social support, routine, and sleep as protective factors. Shared meals and ritual as cohesion practice.

**Illustration slots.** `16-plate-01` — the morale checklist as a weekly grid, the day off marked in orange. `16-gag-01` — the weekly dinner, mismatched chairs, a table made from a door, nobody explaining it. `16-gag-02` — Vera's wrench, hung on a nail, uncaptioned.

---

> ## REVIEW CHECKPOINT — end of Part IV
>
> Stop. Do not begin Task 25.
>
> Run the full tooling pass. Report word counts for chapters 1–16 and the running total against the 45k–55k target.
>
> Ask the user to read chapters 13–16 and confirm: does chapter 15 stay on the right side of the coercion line? Does Vera's death land at the right weight — one line, not a scene? Does chapter 16 set up Part V so the god-building reads as earned rather than as a gag reel?
>
> This is the last checkpoint before the book's thesis chapters. Resolve any doubt about Part V's tone here.

---

## Task 25: Chapter 17 — The Silhouette of Belonging

**Files:**
- Create: `manuscript/17-silhouette.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** Part V opens with the most absurd-sounding practical advice in the book, delivered completely straight: your group needs to be identifiable at three hundred yards, and you should decide what that looks like on purpose. Open with the Spoke's missing spoke — a five-spoke hub with one gap, painted on everything they owned — and his realization, decades later, that it was the most efficient piece of infrastructure they had.

Instruction: why a visible marker is genuinely useful — recognition at distance reduces the number of tense first contacts, which is the leading cause of accidental violence between groups; it signals that a place is claimed and maintained; and it gives the wearer something to belong to, which he notes is not a soft benefit. Then the actual design guidance, treated as a technical problem: silhouette over detail because detail disappears at distance; one high-contrast element; something reproducible by hand with materials you will still have in five years; something that works on a person, a vehicle, a gate, and a grave. The adoption problem, which is the real content: a marker imposed is a uniform and is resented, a marker adopted spreads — so you seed it rather than mandate it, and you let the first versions be ugly. Then the costs, which are serious and get full weight: a marker makes you identifiable to people you would rather were confused, it makes defection visible and therefore costly, and a group that polices its own dress code has started doing something else. He is specific that the Ninth Hand's handprint began as exactly the advice in this chapter.

**Rules.** Introduces **Rule 49: Decide your silhouette before someone decides it for you.** and **Rule 35: Seed it. Do not mandate it.**

**Accuracy entries.** In-group signaling and identity markers as documented anthropological function. Distance recognition reducing threat escalation. Costly-signal and uniform-conformity dynamics, including the coercion risk.

**Illustration slots.** `17-plate-01` — four marks at three hundred yards and at ten feet, showing which survive distance, with the design principles numbered. `17-plate-02` — the same mark applied to a person, a vehicle, a gate, and a grave marker. `17-gag-01` — a comparison chart of six faction silhouettes, each captioned with a one-line assessment, the last one simply AVOID.

---

## Task 26: Chapter 18 — On the Manufacture of Gods

**Files:**
- Create: `manuscript/18-gods.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The book's centerpiece and its most delicate balance. Mother Furnace was invented in an afternoon, by four tired people, for morale, and she is still worshipped by people who would be appalled to hear she was designed. The narrator knows she is fabricated. He also knows she worked, and the chapter's whole achievement is holding both of those at once without a wink.

Open on the afternoon itself: the Bell Country's eleventh year, the foundry nobody wanted to maintain, and the decision to make the furnace sacred because exhortation had failed and reverence had not been tried. It worked within a month. The foundry has not gone cold in thirty years.

Instruction, delivered as straight-faced engineering: what a functioning god actually does for a group — it encodes a practice that must not lapse, it moves the authority for a rule outside any living person's hands, which he notes is the single most useful property, and it gives people a shape for fear. Then the design guidance: attach the deity to a real and necessary practice, because a god with no maintenance duty attached is just a story; give it a domain narrow enough to be useful and wide enough to matter; make its demands cheap, frequent, and physical; make its origin story short, visual, and repeatable by a child; and give it a form that is an object rather than a face, which is why Mother Furnace is a wheel and not a woman. The origin-story workshop, done as an actual procedure — three beats, one impossible detail, one true detail, and a hole left deliberately for other people to fill in, because a story people can add to becomes theirs.

Then the costs, which are the chapter's moral spine and get as much room as the technique: a god cannot be recalled; it will be interpreted by people you will never meet, in ways you would hate; somebody will eventually claim to speak for it, and that person will be the problem; and the gap between a god that asks for maintenance and one that asks for obedience is one generation wide. He states plainly that the Ninth Hand's god was built on identical principles by someone who made different choices, and that the difference was never theology — it was whether the god's demands cost its priests anything. His own line, offered without ceremony: build a god that asks something of you first.

**Rules.** Introduces **Rule 73: A god with no chore attached is a story.** and **Rule 66: If no one can speak for it, no one can speak with it.**

**Accuracy entries.** Ritual and shared belief as documented mechanisms of group cohesion and norm enforcement. Costly-signal theory. Depersonalized authority and rule stability. The institutionalization-to-coercion pathway, cited as the real basis for the chapter's cost section.

**Illustration slots.** `18-plate-01` — the god-design worksheet, filled in for Mother Furnace, five numbered fields. `18-plate-02` — the origin-story structure: three beats, the impossible detail, the true detail, and the deliberate hole, drawn as a diagram. `18-gag-01` — Mother Furnace's official icon, the six-spoke wheel with the furnace door, rendered with total devotional seriousness. `18-gag-02` — the same icon as four regional variants, progressively more elaborate and less correct, the last one barely a wheel.

**Banned moves for this chapter.** No wink. Not one. The narrator never signals that this is a joke, because to him it is not. No instruction that would help someone extract obedience — every technique is attached to a maintenance duty, and the cost section is never shorter than the method section.

---

## Task 27: Chapter 19 — Holidays, Songs, and Other Load-Bearing Nonsense

**Files:**
- Create: `manuscript/19-holidays.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The warmest chapter in the book, and the one that makes its argument almost without arguing. Open with the Bell Country's winter feast, which was invented to use up food that would have spoiled anyway, and which outlived the Bell Country itself — people who never lived there still keep it, and most of them do not know what it was for.

Instruction: a ritual calendar as actual infrastructure — marking the year so people know where they are in it, scheduling rest so it is not a negotiation every time, and the specific value of a holiday that falls at the hardest point of the year rather than the easiest. How to build one that survives: tie it to something unavoidable like a solstice or a harvest, make it cheap, give it one piece of required nonsense that serves no purpose at all (which he insists is the load-bearing part, because a rule with a reason can be argued out of and a rule with no reason cannot), and let it be inherited rather than announced. Then songs, treated with the same engineering seriousness: work songs for synchronizing physical labor, counting songs for teaching procedures to people who cannot read, and the chapter's quietly useful point that the water-treatment chapter has a song in the Bell Country and the children get the boil time right every time. Naming: of children, of places, of years, and why a group that names its years has a memory. Oaths as a commitment device, kept short, public, and bounded, with the real caution that an unbounded oath is a trap and that he has seen them used as one.

**Rules.** Introduces **Rule 59: Put the holiday at the worst part of the year.** and **Rule 18: Teach the children the boil time as a song.**

**Accuracy entries.** Ritual and collective effervescence as cohesion mechanisms. Synchronized labor and work songs. Song and rhyme as mnemonic transmission for procedural knowledge in oral cultures. Commitment devices, and the risk of unbounded ones.

**Illustration slots.** `19-plate-01` — the ritual year as a wheel, the hardest month marked in orange with the feast on it. `19-plate-02` — the boil-time song written out as a simple notated verse, legible and genuinely singable. `19-gag-01` — the required piece of nonsense: everyone at the feast wearing one shoe, no explanation given, nobody questioning it.

---

## Task 28: Chapter 20 — Teaching the Ones Who Never Saw a Lightbulb

**Files:**
- Create: `manuscript/20-teaching.md`
- Modify: `notes/accuracy-log.md`, `notes/continuity.md`

**Brief.** The book's last chapter, addressed to Ais, and the only one written to a person rather than to a reader. It closes everything: the editor of the front matter is of her generation, which means the found manuscript's frame completes here without the narrator ever knowing it.

Open with the discovery that she does not believe in refrigerators. Not disbelieves — she has no slot for the idea, the way he has no slot for what her generation finds obvious. That gap is the chapter's subject.

Instruction: teaching as transmission under loss — assume every explanation that depends on a thing they have never seen will fail, and teach from what is in the room. Apprenticeship over instruction, because a procedure watched and done beats a procedure explained, and his specific sequence of watch, assist, lead, teach, with the note that nobody owns a skill until they have taught it. What to write down and what not to bother with: procedures and numbers written, judgment taught in person, and the brutal triage of deciding which knowledge is worth the paper. The failure he actually fears, stated plainly — not that the knowledge is lost but that it survives as ritual with the reason stripped out, people boiling water for three minutes because the song says so, with no one left who knows about altitude. His countermeasure is the only thing he asks of the reader: write down the why next to the what, even when it costs more paper, because the why is what lets the next generation correct you. Then the handoff. He is old, the book is finished, and he says what he thinks it was for.

And then **Rule 80**, held in reserve for the entire book, spent here. It is the soft rule that outranks all the hard ones and it is the thesis in one line — that the nonsense was the point, that what kept people alive was each other and the ridiculous things they did together, and that he would have been dead in year two without a weekly dinner nobody could justify. Write the reserved rule's text in this task, add it to the ledger, and keep it short. The book opens with rules about not bleeding to death and closes with this one.

**Rules.** Cites **Rule 80** (reserved; text written here). May cite earlier Rules by number in the closing. No other new Rules — the corpus closes.

**Accuracy entries.** Apprenticeship and the watch/assist/lead/teach progression as documented skill transmission. Oral transmission drift and loss of rationale. Teaching from available referents.

**Illustration slots.** `20-plate-01` — the watch/assist/lead/teach progression as four numbered panels, the fourth panel showing the student teaching someone else. `20-gag-01` — Ais, too-large coat, satchel of papers, looking at a drawing of a refrigerator with polite skepticism. `20-gag-02` — the last page of the manuscript, water-damaged at one corner, Rule 80 legible.

---

## Task 29: Appendices

**Files:**
- Create: `manuscript/99-appendices.md`
- Modify: `notes/accuracy-log.md`

**Interfaces:**
- Consumes: the completed `notes/continuity.md` Rule ledger and every chapter's reference tables.
- Produces: the book's back matter. Exempt from apparatus and word-count rules — the linter does not check `99-`.

- [ ] **Step 1: Write Appendix A — The Rules, As Best I Remember Them**

Every Rule in the `notes/continuity.md` ledger, in numerical order, with the gaps left visible: the numbering runs to 80 and most numbers are absent. Gaps are annotated sparingly — most say nothing at all, a few say `[forgotten]`, and exactly two are marked `[page torn]`. One of the torn ones should sit immediately before a Rule the reader will badly want the context for. Rule 80 is last and sits alone.

- [ ] **Step 2: Write Appendix B — Reference tables**

Pull the numeric content out of the chapters, each table captioned with its chapter number so the reader can go read the caveats: water treatment (boil times with altitude, bleach dose and contact time with the cloudy-water caveat restated), bleeding control sequence, oral rehydration ratio, calorie ranges, latrine siting distances, fuel shelf life. Every figure must match its chapter exactly — any discrepancy is a defect in one of the two places. Head the appendix with one line in the narrator's voice noting that the tables are stripped of their warnings and the warnings were the point.

- [ ] **Step 3: Write Appendix C — The god-design worksheet**

Blank, five numbered fields matching chapter 18's plate: the practice it protects, its domain, its demands (cheap, frequent, physical), its origin story in three beats, and its form as an object. Below the fields, one line: the cost question — *what does this god ask of the person who made it?* — with space to answer.

- [ ] **Step 4: Verify tables against chapters**

Run: `python3 scripts/lint_manuscript.py && python3 -m pytest tests/ -q`
Then manually diff every figure in Appendix B against its source chapter and the accuracy log. Fix any mismatch at both ends.

- [ ] **Step 5: Commit**

```bash
git add manuscript/99-appendices.md notes/accuracy-log.md
git commit -m "Add appendices: the Rules, reference tables, god-design worksheet"
```

---

## Task 30: Final pass

**Files:**
- Modify: any chapter requiring correction
- Create: `notes/final-pass.md`

**Interfaces:**
- Consumes: the complete manuscript and all tooling.
- Produces: a completion report against the spec's definition of done.

- [ ] **Step 1: Run everything**

```bash
python3 -m pytest tests/ -q
python3 scripts/lint_manuscript.py
python3 scripts/collect_illos.py
```
Expected: tests pass; linter prints `Manuscript clean.` and exits 0; the collector reports roughly 60 slots.

- [ ] **Step 2: Report the numbers**

```bash
for f in manuscript/*.md; do printf "%-28s %s\n" "$(basename $f)" "$(python3 -c "
import sys; sys.path.insert(0,'scripts')
from illo_blocks import strip_comments
print(len(strip_comments(open('$f').read()).split()))
")"; done
```
Confirm the total lands in 45,000–55,000 words including front and back matter.

- [ ] **Step 3: Read for the things the linter cannot see**

Check and fix: exactly one dark aside per chapter, no more; no winking anywhere, especially chapter 18; the Ninth Hand thread building coherently across chapters 4, 7, 15, 17, and 18; Vera present in 10 and 16 and absent after; Ais named rarely before chapter 20; no two Rules contradicting each other; every chapter's opening naming a specific person.

- [ ] **Step 4: Verify the book reads without images**

Confirm `illustrations/` is empty, then read three chapters start to finish — one from Part I, one from Part III, one from Part V — checking that no sentence depends on an image. Fix any that do. This is the spec's hard requirement and the easiest one to violate by accident.

- [ ] **Step 5: Write `notes/final-pass.md`**

The spec's definition of done as a checklist, each line marked with its evidence: chapter count, word total, apparatus completeness (linter clean), accuracy-log coverage (every chapter has entries, no `_No entries yet._` remaining), illustration slots placed with prompts, manifest generating cleanly, and the no-images read-through confirmed.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "Final pass: manuscript complete, 20 chapters, linter clean"
```

---

## Self-Review

**Spec coverage.** Premise and the never-ironic rule → Global Constraints, Task 5. Framing device → Task 8. Tone register and the one dark aside → Task 5, verified in Task 30. Tone touchstones → Task 5. Structure, all 20 chapters → Tasks 9–28, one each, in spec order. Front matter's three parts → Task 8. Back matter's three appendices → Task 29. Voice rules → Task 5. The Rules device, ledger, and reserved Rule 80 → Task 6 seeds it, Task 3 enforces it, Task 28 spends it, Task 29 lists it. Per-chapter apparatus → Task 5 template, Task 2 enforcement. Recurring cast → Task 6, threaded through the briefs, verified in Task 30. Accuracy discipline and the log → Global Constraints, Task 6, enforced by Task 3, per-chapter entries in every chapter task. Content boundaries → Global Constraints, with chapter-specific banned-move notes in Tasks 11, 18, 23, and 26. Illustration style DNA, classes, consistency plan, and placeholders → Task 7, enforced by Task 3, collected by Task 4. Repo layout → the File Structure table. Workflow's three points → bibles in Tasks 5–7 before chapter 1, one commit per chapter, four Part checkpoints. Definition of done → Task 30.

Two spec items are deliberately out of scope and stated as such in the spec itself: image generation, and the `illustrations/` directory's contents.

**Placeholder scan.** No TBDs. Every code step carries runnable code. Every prose step carries its actual brief, Rules, accuracy entries, and illustration slots rather than a pointer. The chapter steps are factored into a named template once and referenced by number — the full step text is in the template section, not elided. The only intentional blank is Rule 80's text, which Task 6 explicitly reserves and Task 28 explicitly writes; that is a plot requirement, not a missing detail.

**Type consistency.** `parse_blocks` / `IlloBlock` / `strip_comments` / `ID_RE` defined in Task 1 and consumed under those exact names in Tasks 2, 3, and 4. `IlloBlock.cls` (not `class`, which is reserved) used consistently; the manifest's JSON key is `"class"`, converted in `collect_illos.collect`. `read_order` defined in Task 2, imported by Task 4. `CHAPTER_RULES` defined in Task 2, extended in Task 3's `lint()` rewrite. Error-string format `"<file>: <RULE>: <message>"` used by every rule and asserted against in the tests. `LEDGER_ROW_RE` in Task 3 matches the table format Task 6 writes. `ACCURACY_HEADING_RE` matches the `## Chapter NN` headings Task 6 writes. ILLO id token is `plate`/`gag` and `class` must equal that token — one vocabulary, checked by `check_illo_blocks`; the spec's human-facing word "marginalia" maps to `gag` and that mapping is stated in Task 7.
