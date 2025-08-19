---
layout: default
title: Key management
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Key management

Store a key in the environment (for one session):

```
export API_KEY="your-api-key"
```

To store a key across sessions, add the `export API_KEY="your-api-key"` statement to `~/.bash_profile` or `~/.profile`.

{: .info }
> **Common key variables for local setup**
> 
> export OPENAI_KEY="XXX"
> export GITHUB_TOKEN="XXX"

Access the key in Python:

```
import os

api_key = os.environ.get('API_KEY')
```

{: .info }
> Advantage: confidential keys are not saved in the script and not shared with others.
