---
layout: default
title: Pandoc Word Template
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Pandoc Word Template

Pandoc supports Word templates (aka **reference-doc**) for efficient formatting. (see [docs](https://pandoc.org/MANUAL.html){: target="_blank"} `--reference-doc=FILE|URL`, `DOCX`).

It is helpful to:

- Check the style name in the generated Word document.
- Open the Word [styles gallery](https://support.microsoft.com/en-us/office/add-and-remove-styles-from-the-quick-styles-gallery-21c5b9de-b19e-4575-bc87-cb2b55ece224){: target="_blank"} to modify styles.

>[!Note]
> Pandoc reference documents do not support every detailed formatting step(such as tables).
> And they don't have to! We simply reserve some time to format the final document (once) and work in Git/Markdown.

We store templates for IS journals in the [templates](https://github.com/digital-work-lab/templates){: target="_blank"} repository.

## Resources

- [Guideline for creating templates](https://bookdown.org/yihui/rmarkdown-cookbook/word-template.html){: target="_blank"}
