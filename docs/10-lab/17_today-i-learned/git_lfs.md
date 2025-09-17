---
layout: default
title: Git LFS
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Git LFS

## Activation

```
# once per machine
git lfs install

# activate
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Track PDFs via Git LFS"

# add PDFs as usual
git add path/to/file.pdf
git commit -m "Add PDF (LFS)"
git push
````

## Migration with git-filter-repo (PDFs committed without lfs)

```
# install git-filter-repo
sudo apt install git-filter-repo


# migrate pdfs
git lfs migrate import --include="*.pdf"

# list files managed by lfs
git lfs ls-files
```
