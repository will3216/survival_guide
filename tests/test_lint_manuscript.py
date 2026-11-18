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
