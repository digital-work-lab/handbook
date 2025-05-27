---
layout: default
title: UV (Python)
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# UV (Python)

UV is useful for package and virtual environment management.

It allows users to specify dependencies at the beginning of a module and call it as a script (uv automatically installs the dependencies):

```
uv run module_script.py
```

```
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
# ]
# ///

import pandas
...
```
