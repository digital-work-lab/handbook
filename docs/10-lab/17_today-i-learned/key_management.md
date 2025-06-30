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

Access the key in Python:

```
import os

api_key = os.environ.get('API_KEY')
```

{: .info }
> Advantage: confidential keys are not saved in the script and not shared with others.