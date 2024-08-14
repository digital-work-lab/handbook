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
flowchart TB

    subgraph Research
        Writing["<a href='20_processes/20.29.writing.html'>Writing</a>"] --> Data
        Methods["<a href='20_processes/20.18.methods.html'>Methods</a>"] --> Writing
        Data["<a href='20_processes/20.17.data.html'>Data</a>"] --> Methods
    end

    Research --- Collaborating["<a href='20_processes/20.16.collaboration.html'>Collaborating</a>"]
    Projects[("<a href='25-projects.html'>Projects</a>")]
    Research --- Projects

    Resources[("Resources:<br><a href='22-literature.html'>Literature</a>, <a href='23-data.html'>Data</a>, <a href='24-software.html'>Software</a>")] --> Research
    Setup["<a href='20_processes/20.15.repo-setup.html'>Repository setup</a>"] --> Research
    Research --> Submission["<a href='20_processes/20.30.pre-submission.html'>Submission</a>"]
    Submission --> Review["<a href='../50-service/50_processes/50.10.reviewer.html'>Peer review</a>"]
    Review -->|Accept| Publication["<a href='20_processes/20.33.publication.html'>Publication</a>"]
    Review -->|Reject/Revise| Revise["<a href='20_processes/20.32.revision.html'>Revision</a>"]
    Revise --> Research
    
    Publication --> Presentation["<a href='20_processes/20.28.presentation.html'>Presentation</a>"]
    Publication --> Dissemination["<a href='20_processes/20.34.dissemination.html'>Dissemination</a>"]
    Publication --> PublicationOutput["<a href='29-publications.html'>Publication output</a>"]
    Publication --> Improvement["<a href='../10-lab/10_processes/10.01.goals.html'>♻️</a> <a href='20_processes/20.35.improvement.html'>Improvement</a>"] --> Research

```
