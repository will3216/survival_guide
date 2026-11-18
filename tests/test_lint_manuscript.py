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


def test_illo_block_with_unknown_key_is_an_error(monkeypatch):
    # With the parser fixed, an unknown key can no longer arise from ordinary
    # text (that's the point of the fix). This check is belt-and-suspenders:
    # if a block somehow still carries an unknown key (e.g. a future parser
    # regression), the lint must still fail loudly. Simulate that directly.
    import illo_blocks

    block = illo_blocks.IlloBlock(
        id="04-plate-01",
        cls="plate",
        caption="Figure 4.1 - The filter.",
        alt="A cutaway of a barrel filter.",
        prompt="Cutaway diagram of a three-layer water filter.",
        raw_keys={
            "id": "04-plate-01",
            "class": "plate",
            "caption": "Figure 4.1 - The filter.",
            "alt": "A cutaway of a barrel filter.",
            "prompt": "Cutaway diagram of a three-layer water filter.",
            "bottom": "the left-hand one shows a pot.",
        },
        line=1,
        following_lines=["![Figure 4.1 - The filter.](../illustrations/04-plate-01.png)"],
    )
    monkeypatch.setattr(lint, "parse_blocks", lambda text: [block])
    errors = lint.check_illo_blocks("04-water.md", "irrelevant")
    assert any("ILLO" in e and "bottom" in e for e in errors)


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
