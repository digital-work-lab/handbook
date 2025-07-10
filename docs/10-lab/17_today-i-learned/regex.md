---
layout: default
title: Regex
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Regex

A useful tool for developing, analyzing and testing regex is [regex101.com](https://regex101.com/).

Python supports named groups:

```Python
import re

text = "Today's date is 2025-07-10."

pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, text)

if match:
    print("Year:", match.group("year"))
    print("Month:", match.group("month"))
    print("Day:", match.group("day"))
```