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
