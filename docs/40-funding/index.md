---
layout: default
title: Funding
has_children: true
has_toc: true
nav_order: 40
---

# Funding

{: .text-center}
```mermaid
flowchart LR
    subgraph pre_award
        Search --> Apply
    end
    
    Apply --> Manage
    
    subgraph post_award
        Manage --> Close
    end
    Close --> Search
```
