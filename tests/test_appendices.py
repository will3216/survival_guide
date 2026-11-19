"""Invariants binding manuscript/99-appendices.md to notes/continuity.md.

Appendix A is the only place in this book where one file must be a verbatim
transcription of another. The ledger it transcribes is a long note that later
work will keep editing, so a single word changed in a row leaves the appendix
silently wrong with nothing in the build to say so. These tests are that
something.

They also hold the two torn gaps open. The gaps are the payoff of the
preface's best line and the book must never reveal what either Rule said, so
the destructive edit to guard against is not a stray citation — the linter
already catches those — it is somebody adding a ledger row inside a gap and
writing it into the list, which would lint perfectly clean. The assertion is
therefore made on the ledger itself.
"""

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

LEDGER_ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|$")
APPENDIX_ROW_RE = re.compile(r"^- \*\*(\d{1,3})\.\*\* (.+)$", re.MULTILINE)
LAST_RULE_RE = re.compile(r"^\*\*(\d{1,3})\.\*\* (.+)$", re.MULTILINE)
TABLE_HEADING_RE = re.compile(r"^### Table \d+ — .*$", re.MULTILINE)

# The two torn pages. Neither gap's number is determinate, which is how the
# book keeps the torn Rules unrecoverable: one gap sits between Rule 38 and
# Rule 42, the other between Rule 77 and Rule 80. No Rule may ever be written
# into these runs. See notes/continuity.md, 'Appendices, now fixed'.
TORN_RUNS = (range(39, 42), range(78, 80))

EXPECTED_RULE_COUNT = 37
EXPECTED_TORN_MARKS = 2
EXPECTED_FORGOTTEN_MARKS = 4


@pytest.fixture(scope="module")
def appendix() -> str:
    return (ROOT / "manuscript" / "99-appendices.md").read_text()


@pytest.fixture(scope="module")
def ledger() -> list[tuple[int, str]]:
    rows = []
    for line in (ROOT / "notes" / "continuity.md").read_text().splitlines():
        match = LEDGER_ROW_RE.match(line.strip())
        if match:
            rows.append((int(match.group(1)), match.group(2)))
    return rows


def appendix_rules(text: str) -> list[tuple[int, str]]:
    rules = [(int(n), t) for n, t in APPENDIX_ROW_RE.findall(text)]
    rules += [(int(n), t) for n, t in LAST_RULE_RE.findall(text)]
    return rules


def test_appendix_a_transcribes_the_ledger_exactly(appendix, ledger):
    """Numbers, text and order, with no drift in any of the three."""
    assert appendix_rules(appendix) == sorted(ledger)


def test_the_ledger_is_closed_at_thirty_seven_rules(appendix, ledger):
    numbers = [n for n, _ in ledger]
    assert len(ledger) == EXPECTED_RULE_COUNT
    assert len(set(numbers)) == EXPECTED_RULE_COUNT
    assert max(numbers) == 80
    assert len(appendix_rules(appendix)) == EXPECTED_RULE_COUNT


def test_no_rule_exists_inside_either_torn_gap(ledger):
    """The contents of the two torn Rules are never to be written down.

    Not in the manuscript, not in the ledger, not anywhere. A new ledger row
    inside either run would both invent a Rule the book says is lost and
    narrow which number was taken.
    """
    numbers = {n for n, _ in ledger}
    for run in TORN_RUNS:
        inside = sorted(numbers & set(run))
        assert inside == [], f"ledger row(s) {inside} written into a torn gap"


def test_the_gap_marks_keep_their_counts(appendix):
    """Exactly two torn, exactly four forgotten.

    The two is fixed by the preface, which says two pages were torn out. The
    four is his own forgetting, and a later pass 'balancing' the annotations
    is as destructive as one filling a gap.
    """
    assert appendix.count("[page torn") == EXPECTED_TORN_MARKS
    assert appendix.count("[forgotten") == EXPECTED_FORGOTTEN_MARKS


def test_neither_gap_mark_is_annotated(appendix):
    """Both marks are bare, and neither is signed.

    A signature on the torn mark makes it the only non-Rule text to repeat in
    the list, which turns the gap into a caption and points the apparatus at
    the thing the preface already mourned.
    """
    for mark in ("[page torn", "[forgotten"):
        lines = [l.strip() for l in appendix.splitlines() if mark in l]
        assert lines, mark
        for line in lines:
            assert line == f"- *{mark}]*", line


def test_one_torn_gap_sits_immediately_before_the_last_rule(appendix):
    """The preface's payoff: the gap adjacent to the book's closing Rule."""
    marks = [l.strip() for l in appendix.splitlines() if l.strip()]
    index = marks.index("**80.** Go to the daft dinner.")
    assert marks[index - 1] == "- *[page torn]*"


def test_every_appendix_b_table_names_its_chapter(appendix):
    """The reader's route back to the caveats.

    The tables are stripped of their warnings by design, so the chapter
    number in the caption is the only thing that gets a reader to them. A
    pass that tightens the captions must not take it.
    """
    headings = TABLE_HEADING_RE.findall(appendix)
    assert headings
    for heading in headings:
        assert re.search(r"Chapter \d{1,2}\.$", heading), heading
