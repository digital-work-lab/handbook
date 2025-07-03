---
layout: default
title: Convert spreadsheet coding to obsidian notes
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Convert spreadsheet coding to obsidian notes

To convert tabular coding of papers (in a spreadsheet) to obsidian notes, the following script may be helpful:


```python
import ezodf
from pathlib import Path

# Set paths
ods_file_path = "filename.ods"  # Replace with your ODS filename
output_dir = Path("obsidian_summaries")


output_dir.mkdir(exist_ok=True)
doc = ezodf.opendoc(ods_file_path)
sheet = doc.sheets["summary"]

rows = list(sheet.rows())
headers = [cell.value.strip() if cell.value else "" for cell in rows[0]]

# Column helper
def get_cell_value(row, column_name):
    try:
        idx = headers.index(column_name)
        return row[idx].value if idx < len(row) else ""
    except ValueError:
        return ""

for i, row in enumerate(rows[1:], start=1):
    citation_key = get_cell_value(row, "citation_key") or f"Paper_{i}"
    keywords = get_cell_value(row, "keywords") or ""
    summary = get_cell_value(row, "summary") or ""
    quotes = get_cell_value(row, "quotes") or ""
    if quotes:
        quotes = f"# Quotes\n\n{quotes}"

    # Skip if empty citation_key
    if not citation_key.strip():
        continue

    file_name = f"{citation_key.strip().replace(' ', '_')}.md"
    file_path = output_dir / file_name

    content = f"""---
title:         "{citation_key}"
keywords:      {keywords}

---

# Summary:

{summary}

{quotes}"""
    file_path.write_text(content.strip(), encoding="utf-8")

print(f"✅ Done. Files written to {output_dir.resolve()}")
```