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
