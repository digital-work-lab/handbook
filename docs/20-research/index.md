---
layout: default
title: Research
has_children: true
has_toc: true
nav_order: 20
---

# Research

Projects are in [25-Projects](25-projects.html) and can be in the following states:

{: .text-center}
```mermaid

flowchart LR
    subgraph Projects
        direction TB
        Concept(["<a href='#concept'>Concept</a>"]) -.-> Writing(["<a href='#writing'>Writing</a>"])
        Writing --> OnHold(["<a href='#on-hold'>On Hold</a>"])
        OnHold --> Writing
        OnHold -.-> Abandoned(["<a href='#abandoned'>Abandoned</a>"])
        Writing ==> UnderReview(["<a href='#under-review'>Under review</a>"])
        Revising -.-> OnHold
        Revising ==> UnderReview
        UnderReview ==> Revising(["<a href='#revising'>Revising</a>"])
        Revising ==> Published(["<a href='#published'>Published</a>"])
    end
    style Projects fill:white,stroke:#333,stroke-width:3px

```
<!-- TODO: Cover Research data management, and reproducibility (but check with the team before publishing data - make sure confidential data is protected) -->

## Concept

- [Goals](20_processes/20.01.goals.html)
- [Ideas](20_processes/20.09.ideas.html)
- Selection
- [Repository setup](20_processes/20.15.repo-setup.html)

## Writing

- [Collaboration](20_processes/20.16.collaboration.html)
- [Software](24-software.html)
- [Literature](22-literature.html)
- [Methods](20_processes/20.18.methods.html)
- [Data management](20_processes/20.17.data.html) - [Data sets](23-data.html)
- [Writing](20_processes/20.29.writing.html)
- [Submission](20_processes/20.30.pre-submission.html)

## Under Review

## Revising

- [Revision](20_processes/20.32.revision.html)

## On Hold

## Abandoned

## Published

- [Improvement](20_processes/20.35.improvement.html) <a href='{{ site.baseurl }}/docs/00.goals.html'>♻️</a>
- [Publication](20_processes/20.33.publication.html)
- [Presentation](20_processes/20.28.presentation.html)
- [Dissemination](20_processes/20.34.dissemination.html)
- [Publication Output](29-publications.html)
