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

# Old raw base (we can keep it as secondary/fallback)
RAW_BASE_URL = "https://raw.githubusercontent.com/digital-work-lab/handbook/main/docs/"

# NEW: serve markdown from the same origin as the RAG JSON
# this assumes you publish the `docs/` folder to GitHub Pages under /handbook/docs/
PAGES_MD_BASE_URL = "https://digital-work-lab.github.io/handbook/docs/"

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

    all_sections = []

    for entry in sorted(DOCS_DIR.iterdir()):
        # ----- CASE 1: top-level single .md -----
        if entry.is_file() and entry.suffix == ".md":
            section = entry.name.replace(".md", "")  # e.g. "00.goals"
            section_dir = RAG_ROOT / section
            section_dir.mkdir(parents=True, exist_ok=True)

            rel_path = entry.relative_to(DOCS_DIR)  # e.g. 00.goals.md
            raw_url = RAW_BASE_URL + str(rel_path)
            md_url = PAGES_MD_BASE_URL + str(rel_path)

            text = md_to_text(entry.read_text(encoding="utf-8"))
            chunks = chunk_text(text)
            records = []
            for i, ch in enumerate(chunks):
                emb = model.encode(ch).tolist()
                records.append({
                    "source": str(rel_path),
                    "chunk_id": i,
                    "text": ch,
                    "embedding": emb
                })

            # per-file rag json
            section_file_name = f"{section}.json"
            (section_dir / section_file_name).write_text(
                json.dumps({
                    "model": MODEL_NAME,
                    "section": section,
                    "file": str(rel_path),
                    # primary for clients:
                    "md_url": md_url,
                    # optional fallback:
                    "raw_url": raw_url,
                    "records": records
                }, indent=2),
                encoding="utf-8",
            )

            # per-section index (only one file)
            (section_dir / "index.json").write_text(
                json.dumps({
                    "model": MODEL_NAME,
                    "section": section,
                    "files": [
                        {
                            "file": str(rel_path),
                            "slug": section,
                            "json": section_file_name,
                            "md_url": md_url,
                            "raw_url": raw_url,
                            "num_records": len(records)
                        }
                    ]
                }, indent=2),
                encoding="utf-8",
            )

            all_sections.append({
                "section": section,
                "index": f"{section}/index.json"
            })

            print(f"wrote {section_dir / 'index.json'} and {section_dir / section_file_name}")
            continue

        # ----- CASE 2: directories like 20-research, 30-teaching, ... -----
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
                rel_inside = md_path.relative_to(DOCS_DIR)   # e.g. 20-research/sub.md
                slug = str(rel_inside).replace("/", "_").replace(".md", "")
                out_file = section_dir / f"{slug}.json"

                raw_url = RAW_BASE_URL + str(rel_inside)
                md_url = PAGES_MD_BASE_URL + str(rel_inside)

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

                # write per-file json with md_url included
                out_file.write_text(
                    json.dumps({
                        "model": MODEL_NAME,
                        "section": section,
                        "file": str(rel_inside),
                        "md_url": md_url,
                        "raw_url": raw_url,
                        "records": records
                    }, indent=2),
                    encoding="utf-8",
                )

                section_index["files"].append({
                    "file": str(rel_inside),
                    "slug": slug,
                    "json": f"{slug}.json",
                    "md_url": md_url,
                    "raw_url": raw_url,
                    "num_records": len(records)
                })

                print(f"wrote {out_file}")

            # write section-level index
            (section_dir / "index.json").write_text(
                json.dumps(section_index, indent=2),
                encoding="utf-8",
            )
            print(f"wrote {section_dir / 'index.json'}")

            all_sections.append({
                "section": section,
                "index": f"{section}/index.json"
            })

    # overarching index
    (RAG_ROOT / "index.json").write_text(
        json.dumps({
            "model": MODEL_NAME,
            "sections": all_sections
        }, indent=2),
        encoding="utf-8",
    )
    print(f"wrote {RAG_ROOT / 'index.json'}")
    print("done.")


if __name__ == "__main__":
    main()
