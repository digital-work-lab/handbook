---
layout: default
title: Python-LLM
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Python-LLM

Reading files (PDF or MD) and using an LLM API to analyze them:

```python
#  pip install openai pymupdf
#  export OPENAI_API_KEY=...

import os
from pathlib import Path
from typing import Iterable
import pymupdf
from openai import OpenAI

client = OpenAI()

ROOT = Path("markdown")
OUT  = Path("findings")
OUT.mkdir(parents=True, exist_ok=True)

MODEL = "gpt-4o"

PROMPT_TEMPLATE = """You are analyzing project notes and papers.
Extract 3–5 bullet points with concrete findings or action items.
Respond in Markdown only (no preamble), using:
- **Summary**: one sentence
- **Key Points**: bullets
- **Evidence**: short quotes if available
"""

# -------- helpers --------
def read_text_from_md(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def read_text_from_pdf(path: Path) -> str:
    text_chunks = []
    with pymupdf.open(path) as doc:
        for page in doc:
            text_chunks.append(page.get_text("text"))
    return "\n".join(text_chunks)

def iter_corpus(root: Path) -> Iterable[Path]:
    exts = {".md", ".pdf"}
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts:
            yield p

def run_llm(model: str, system: str, user: str) -> str:
    # Chat Completions API (widely supported)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content or ""

def main():
    files = list(iter_corpus(ROOT))
    if not files:
        print(f"No .md or .pdf files found under {ROOT.resolve()}")
        return

    for path in files:
        try:
            if path.suffix.lower() == ".md":
                raw_text = read_text_from_md(path)
            elif path.suffix.lower() == ".pdf":
                raw_text = read_text_from_pdf(path)
            else:
                continue

            # keep input small for demo; trim if huge
            snippet = raw_text[:20000]

            prompt = f"{PROMPT_TEMPLATE}\n\n# File: {path.name}\n\n<Content Start>\n{snippet}\n<Content End>"
            findings_md = run_llm(MODEL, "You are a concise research assistant.", prompt)

            out_path = OUT / f"{path.stem}.md"
            out_path.write_text(findings_md.strip() + "\n", encoding="utf-8")
            print(f"✓ Saved: {out_path.relative_to(Path.cwd())}")

        except Exception as e:
            print(f"⚠️ {path}: {e}")

if __name__ == "__main__":
    main()
```