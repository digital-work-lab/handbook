#!/usr/bin/env python3
import json
import pathlib
import re
from typing import List
from sentence_transformers import SentenceTransformer

ROOT = pathlib.Path.cwd()
DOCS_DIR = ROOT / "docs"
RAG_ROOT = ROOT / "rag"
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
    RAG_ROOT.mkdir(parents=True, exist_ok=True)

    for entry in sorted(DOCS_DIR.iterdir()):
        # top-level single markdown files -> make a folder too, for consistency
        if entry.is_file() and entry.suffix == ".md":
            section = entry.name.replace(".md", "")  # e.g. "00.goals"
            section_dir = RAG_ROOT / section
            section_dir.mkdir(parents=True, exist_ok=True)

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

            # write single-file index as index.json
            (section_dir / "index.json").write_text(
                json.dumps({
                    "model": MODEL_NAME,
                    "section": section,
                    "files": [
                        {
                            "file": entry.name,
                            "slug": section,
                            "json": f"{section}.json",
                            "num_records": len(records),
                        }
                    ],
                }, indent=2),
                encoding="utf-8",
            )

            # write the actual rag file
            (section_dir / f"{section}.json").write_text(
                json.dumps({
                    "model": MODEL_NAME,
                    "section": section,
                    "file": entry.name,
                    "records": records,
                }, indent=2),
                encoding="utf-8",
            )

            print(f"wrote {section_dir / 'index.json'} and {section_dir / f'{section}.json'}")
            continue

        # directories like 10-lab, 20-research, ...
        if entry.is_dir():
            section = entry.name
            section_dir = RAG_ROOT / section
            section_dir.mkdir(parents=True, exist_ok=True)

            section_index = {
                "model": MODEL_NAME,
                "section": section,
                "files": []
            }

            for md_path in entry.rglob("*.md"):
                rel_inside = md_path.relative_to(DOCS_DIR)  # e.g. 20-research/some.md
                # slug for filename, safe
                slug = str(rel_inside).replace("/", "_").replace(".md", "")
                out_file = section_dir / f"{slug}.json"

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

                out_file.write_text(
                    json.dumps({
                        "model": MODEL_NAME,
                        "section": section,
                        "file": str(rel_inside),
                        "records": records,
                    }, indent=2),
                    encoding="utf-8",
                )

                section_index["files"].append({
                    "file": str(rel_inside),
                    "slug": slug,
                    "json": f"{slug}.json",
                    "num_records": len(records),
                })
                print(f"wrote {out_file}")

            # write section index in the section dir
            (section_dir / "index.json").write_text(
                json.dumps(section_index, indent=2),
                encoding="utf-8",
            )
            print(f"wrote {section_dir / 'index.json'}")

    print("done.")


if __name__ == "__main__":
    main()
