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
