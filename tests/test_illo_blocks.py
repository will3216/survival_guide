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
