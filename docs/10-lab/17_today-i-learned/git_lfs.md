---
layout: default
title: Git LFS
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Git LFS

```
# install git-filter-repo
sudo apt install git-filter-repo

# migrate pdfs
git lfs migrate import --include="*.pdf"

# list files managed by lfs
git lfs ls-files
```