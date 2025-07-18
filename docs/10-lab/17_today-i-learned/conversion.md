---
layout: default
title: File conversion
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# File conversion

## PDF-to-Markdown

```
docker run --rm -v "$PWD":/data pandoc_dockerfile input.docx -f docx -t markdown --wrap=none -o output.md
```