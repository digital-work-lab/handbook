"""Minimal YAML front matter parser for handbook automation scripts."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import MutableMapping, Union

from ruamel.yaml import YAML


@dataclass
class Post:
    """Container for parsed front matter and Markdown body."""

    metadata: MutableMapping
    content: str


def _read_text(source: Union[str, Path]) -> str:
    path = Path(source)
    return path.read_text(encoding="utf-8")


def load(source: Union[str, Path]) -> Post:
    """Load a Markdown file with YAML front matter."""
    text = _read_text(source)
    if not text:
        return Post(metadata={}, content="")

    lines = text.splitlines()
    fm_lines = []
    body_lines = []

    if lines[0].strip() == "---":
        try:
            end_index = lines.index("---", 1)
            fm_lines = lines[1:end_index]
            body_lines = lines[end_index + 1 :]
        except ValueError:
            fm_lines = lines[1:]
            body_lines = []
    else:
        for idx, line in enumerate(lines):
            if line.strip() == "---":
                fm_lines = lines[:idx]
                body_lines = lines[idx + 1 :]
                break
        else:
            fm_lines = lines
            body_lines = []

    fm_text = "\n".join(fm_lines)
    body = "\n".join(body_lines)

    yaml = YAML()
    yaml.preserve_quotes = True
    metadata = yaml.load(fm_text) if fm_text.strip() else {}
    if metadata is None:
        metadata = {}

    return Post(metadata=metadata, content=body)
