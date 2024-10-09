---
layout: default
title: 24 Software
parent: Research
nav_order: 5
---

# 24 Software
{: .d-inline-block }

We develop software packages, primarily for literature reviews.
Our software is available in the [CoLRev Environment](https://github.com/CoLRev-Environment){: target="_blank"} and the [digital-work lab](https://github.com/orgs/digital-work-lab/repositories){: target="_blank"} organization.

## Collaborative Literature Reviews (CoLRev)

[CoLRev](https://github.com/CoLRev-Environment/colrev){: target="_blank"} is an open-source environment for collaborative literature reviews.
It integrates with different synthesis tools, takes care of the data, and facilitates Git-based collaboration. 
To accomplish these goals, CoLRev advances the design of review technology at the intersection of methods, design, cognition, and community building.
The following features stand out:

- Supports all literature review steps: problem formulation, search, dedupe, (pre)screen, pdf retrieval and preparation, and synthesis
- An open and extensible environment based on shared data and process standards
- Builds on git and its transparent collaboration model for the entire literature review process
- Offers a self-explanatory, fault-tolerant, and configurable user workflow
- Operates a model for data quality, content curation, and reuse
- Enables typological and methodological pluralism throughout the process

## BibDedupe

BibDedupe is an open-source **Python library for deduplication of bibliographic records**, tailored for literature reviews.
Unlike traditional deduplication methods, BibDedupe focuses on entity resolution, linking duplicate records instead of simply deleting them.

- **Automated Duplicate Linking with Zero False Positives**: BibDedupe automates the duplicate linking process with a focus on eliminating false positives.
- **Preprocessing Approach**: BibDedupe uses a preprocessing approach that reflects the unique error generation process in academic databases, such as author re-formatting, journal abbreviation or translations.
- **Entity Resolution**: BibDedupe does not simply delete duplicates, but it links duplicates to resolve the entity and integrates the data. This allows for validation, and undo operations.
- **Programmatic Access**: BibDedupe is designed for seamless integration into existing research workflows, providing programmatic access for easy incorporation into scripts and applications.
- **Transparent and Reproducible Rules**: BibDedupe's blocking and matching rules are transparent and easily reproducible to promote reproducibility in deduplication processes.
- **Continuous Benchmarking**: Continuous integration tests running on GitHub Actions ensure ongoing benchmarking, maintaining the library's reliability and performance across datasets.
- **Efficient and Parallel Computation**: BibDedupe implements computations efficiently and in parallel, using appropriate data structures and functions for optimal performance.

## SearchQuery

Search-query is a Python package for parsing, validating, simplifying, and serializing literature search queries.
It currently supports PubMed and Web of Science, and can be extended to support other databases.
As a default it relies on the JSON schema proposed by an expert panel (Haddaway et al., 2022).
The package can be used programmatically or through the command line, has zero dependencies, and can therefore be integrated in a variety of environments.
<!-- The heuristics, parsers, and linters are battle-tested on over 500 peer-reviewed queries registered at [searchRxiv](https://www.cabidigitallibrary.org/journal/searchrxiv){: target="_blank"}. -->

## Recommended research software

- [R: Tidyverse](https://www.tidyverse.org/){: target="_blank"}
- [rOpenSci](https://ropensci.org/){: target="_blank"}
