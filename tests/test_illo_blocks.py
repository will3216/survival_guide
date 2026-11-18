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


def test_prompt_continuation_with_bottom_colon_is_folded_whole():
    text = """<!-- ILLO
id: 04-plate-02
class: plate
caption: Figure 4.3 - Treating it.
alt: A flowchart.
prompt: Arrows converge and then split into two boxes at the
  bottom: the left-hand one shows a lidded pot with vigorous bubbles,
  numeral 4; the right-hand one shows a covered jar, numeral 5.
-->
"""
    b = illo_blocks.parse_blocks(text)[0]
    assert "bottom" not in b.raw_keys
    assert b.prompt == (
        "Arrows converge and then split into two boxes at the "
        "bottom: the left-hand one shows a lidded pot with vigorous bubbles, "
        "numeral 4; the right-hand one shows a covered jar, numeral 5."
    )


def test_prompt_continuation_with_other_colon_words_is_folded():
    for word in ("left", "note", "top"):
        text = f"""<!-- ILLO
id: 04-plate-03
class: plate
caption: Figure 4.4 - Something.
alt: Something else.
prompt: The first part of the sentence continues onto a line beginning
  {word}: which should not become a new key at all.
-->
"""
        b = illo_blocks.parse_blocks(text)[0]
        assert word not in b.raw_keys, f"{word!r} should not be parsed as a key"
        assert b.prompt == (
            "The first part of the sentence continues onto a line beginning "
            f"{word}: which should not become a new key at all."
        )


def test_all_five_real_keys_parse_normally_with_mid_sentence_colon():
    text = """<!-- ILLO
id: 04-plate-04
class: plate
caption: Figure 4.5 - A caption with a colon: like this.
alt: Alt text with a colon: right here.
prompt: A prompt with a colon: right in the middle of it.
-->
"""
    b = illo_blocks.parse_blocks(text)[0]
    assert b.id == "04-plate-04"
    assert b.cls == "plate"
    assert b.caption == "Figure 4.5 - A caption with a colon: like this."
    assert b.alt == "Alt text with a colon: right here."
    assert b.prompt == "A prompt with a colon: right in the middle of it."
    assert set(b.raw_keys.keys()) == {"id", "class", "caption", "alt", "prompt"}
