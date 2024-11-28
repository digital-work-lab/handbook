---
layout: default
title: Research
has_children: true
has_toc: true
nav_order: 20
---

# Research


{: .text-center}
```mermaid

flowchart LR
    Concept([Concept]) --> Writing([Writing])
    Writing --> UnderReview([Under Review])
    UnderReview --> Revising([Revising])
    Revising --> UnderReview
    Revising --> Published([Published])
    Writing --> OnHold([On Hold])
    Revising --> OnHold
    OnHold --> Abandoned([Abandoned])
    OnHold --> Writing

```

## Concept

- [Goals](20_processes/20.01.goals.html)
- [Ideas](20_processes/20.09.ideas.html)
- Selection
- [Repository setup](20_processes/20.15.repo-setup.html)

<!-- TODO: Cover Research data management, reproducibility (but check with the team before publishing data - make sure confidential data is protected) -->
