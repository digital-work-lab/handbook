#!/usr/bin/env python3
"""
Build per-section RAG indexes from docs/.
- docs/
  - 00.goals.md
  - 01.team.md
  - 02.calendar.md
  - 03.responsibilities.md
  - 10-lab/
  - 20-research/
  - 30-teaching/
  - 40-funding/
  - 50-service/
  - calendar/
Result:
  rag/00.goals.json
  rag/01.team.json
  ...
  rag/10-lab.json
  ...
"""

import json
import pathlib
import re
from typing import List
from sentence_transformers import SentenceTransformer

ROOT = pathlib.Path.cwd()
DOCS_DIR = ROOT / "docs"          # <- adjust if yours is different
RAG_DIR = ROOT / "rag"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def md_to_text(md: str) -> str:
    """Very basic Markdown → text cleaner."""
    md = re.sub(r"```.*?```", "", md, flags=re.DOTALL)   # remove code blocks
    md = re.sub(r"!\[.*?\]\(.*?\)", "", md)              # remove images
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)     # link text only
    md = re.sub(r"#", "", md)
    return md.strip()


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks


def collect_section_entries(section_path: pathlib.Path) -> List[pathlib.Path]:
    """Return all markdown files belonging to this section."""
    if section_path.is_file() and section_path.suffix == ".md":
        return [section_path]
    elif section_path.is_dir():
        return list(section_path.rglob("*.md"))
    else:
        return []


def main():
    # load model once
    model = SentenceTransformer(MODEL_NAME)
    RAG_DIR.mkdir(parents=True, exist_ok=True)

    # iterate over top-level entries in docs/
    for entry in sorted(DOCS_DIR.iterdir()):
        print(f"Indexing {entry}")
        # give every top-level file/dir its own section index
        section_name = entry.name  # e.g. "00.goals.md" or "10-lab"
        # normalize for JSON filename
        section_json_name = section_name.replace(".md", "") + ".json"
        out_file = RAG_DIR / section_json_name

        md_files = collect_section_entries(entry)
        if not md_files:
            # skip if no md files (rare)
            continue

        records = []
        for md_path in md_files:
            raw = md_path.read_text(encoding="utf-8")
            text = md_to_text(raw)
            chunks = chunk_text(text)
            for i, ch in enumerate(chunks):
                emb = model.encode(ch).tolist()
                records.append({
                    "source": str(md_path.relative_to(DOCS_DIR)),
                    "chunk_id": i,
                    "text": ch,
                    "embedding": emb,
                })

        # write per-section file
        out_file.write_text(
            json.dumps(
                {
                    "model": MODEL_NAME,
                    "section": section_name,
                    "records": records,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"wrote {out_file} with {len(records)} chunks")

    print("done.")


if __name__ == "__main__":
    main()
