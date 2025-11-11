#!/usr/bin/env python3
import json
import pathlib
import re
from typing import List
from sentence_transformers import SentenceTransformer

ROOT = pathlib.Path.cwd()
DOCS_DIR = ROOT / "docs"
RAG_DIR = ROOT / "rag"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def md_to_text(md: str) -> str:
    md = re.sub(r"```.*?```", "", md, flags=re.DOTALL)
    md = re.sub(r"!\[.*?\]\(.*?\)", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = re.sub(r"#", "", md)
    return md.strip()


def chunk_text(text: str, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def main():
    model = SentenceTransformer(MODEL_NAME)
    RAG_DIR.mkdir(parents=True, exist_ok=True)

    # iterate over top-level entries in docs
    for entry in sorted(DOCS_DIR.iterdir()):
        # files like 00.goals.md
        if entry.is_file() and entry.suffix == ".md":
            rel = entry.name.replace(".md", "")
            out_file = RAG_DIR / f"{rel}.json"
            text = md_to_text(entry.read_text(encoding="utf-8"))
            chunks = chunk_text(text)
            records = []
            for i, ch in enumerate(chunks):
                emb = model.encode(ch).tolist()
                records.append({
                    "source": str(entry.relative_to(DOCS_DIR)),
                    "chunk_id": i,
                    "text": ch,
                    "embedding": emb
                })
            out_file.write_text(json.dumps({
                "model": MODEL_NAME,
                "section": rel,
                "records": records
            }, indent=2), encoding="utf-8")
            print(f"wrote {out_file}")
            continue

        # directories like 10-lab, 30-teaching, ...
        if entry.is_dir():
            section = entry.name  # e.g. 30-teaching
            section_index = {
                "model": MODEL_NAME,
                "section": section,
                "files": []
            }

            # each .md inside becomes its own RAG file
            for md_path in entry.rglob("*.md"):
                rel_inside = md_path.relative_to(DOCS_DIR)
                # create a safe slug from the relative path
                slug = str(rel_inside).replace("/", "_").replace(".md", "")
                out_file = RAG_DIR / f"{section}.{slug}.json"

                text = md_to_text(md_path.read_text(encoding="utf-8"))
                chunks = chunk_text(text)
                records = []
                for i, ch in enumerate(chunks):
                    emb = model.encode(ch).tolist()
                    records.append({
                        "source": str(rel_inside),
                        "chunk_id": i,
                        "text": ch,
                        "embedding": emb
                    })

                out_file.write_text(json.dumps({
                    "model": MODEL_NAME,
                    "section": section,
                    "file": str(rel_inside),
                    "records": records
                }, indent=2), encoding="utf-8")

                section_index["files"].append({
                    "file": str(rel_inside),
                    "slug": slug,
                    "json": f"{section}.{slug}.json",
                    "num_records": len(records)
                })
                print(f"wrote {out_file}")

            # write the small index for the section
            index_file = RAG_DIR / f"{section}.index.json"
            index_file.write_text(json.dumps(section_index, indent=2), encoding="utf-8")
            print(f"wrote {index_file}")

    print("done.")


if __name__ == "__main__":
    main()
