---
layout: default
title: Key management
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Key management

Store a key in the environment:

```
export API_KEY="your-api-key"
```

```
import os

api_key = os.environ.get('API_KEY')
```
