---
layout: default
title: Research
has_children: true
has_toc: true
nav_order: 3
---

# Research

<!-- TODO: Cover Research data management, reproducibility (but check with the team before publishing data - make sure confidential data is protected) -->

{: .text-center}
```mermaid
flowchart LR

    Research --> Submission["<a href='20_processes/20.30.pre-submission.html'>Submission</a>"]
    subgraph Closing
        direction TB
        Publication["<a href='20_processes/20.33.publication.html'>Publication</a>"]
        Presentation["<a href='20_processes/20.28.presentation.html'>Presentation</a>"]
        Dissemination["<a href='20_processes/20.34.dissemination.html'>Dissemination</a>"]
        Improvement["<a href='../10-lab/10_processes/10.01.goals.html'>♻️</a> <a href='20_processes/20.35.improvement.html'>Improvement</a>"]
    end
    Publication --> PublicationOutput["<a href='29-publications.html'>Publication output</a>"]
    subgraph Research["Research (<a href='25-projects.html'>Projects</a>)"]
        direction LR
        Resources[("Resources:<br><ul><li><a href='22-literature.html'>Literature</a></li><li><a href='23-data.html'>Data</a></li><li><a href='24-software.html'>Software</a></li><li><a href='20_processes/20.16.collaboration.html'>Collaborating</a></li></ul>")]
        Writing["<a href='20_processes/20.29.writing.html'>Writing</a>"] --> Data
        Methods["<a href='20_processes/20.18.methods.html'>Methods</a>"] --> Writing
        Data["<a href='20_processes/20.17.data.html'>Data</a>"] --> Methods
        Submission <-->|Reject/Revise| Revise["<a href='20_processes/20.32.revision.html'>Revision</a>"]
    end
    Submission -->|Accept| Closing

    subgraph Proposal
        direction TB
        Goals --> Approval
        Ideas["<a href='20_processes/20.09.ideas.html'>Ideas</a>"] --> Approval
        Approval --> Setup["<a href='20_processes/20.15.repo-setup.html'>Repository setup</a>"]
    end
    Setup --- Research
```
