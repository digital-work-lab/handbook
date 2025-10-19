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

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/CoLRev-Ecosystem/colrev/main/docs/figures/logo_small.png" alt="CoLRev Logo" width="300"></td>
    <td>
      <a href="https://github.com/CoLRev-Environment/colrev"><img src="https://img.shields.io/github/commit-activity/t/CoLRev-Environment/colrev" alt="Total commits"></a><br>
      <a href="https://github.com/CoLRev-Environment/colrev"><img src="https://img.shields.io/github/contributors-anon/CoLRev-Environment/colrev" alt="Contributors"></a><br>
      <a href="https://zenodo.org/badge/latestdoi/363073613"><img src="https://zenodo.org/badge/363073613.svg" alt="DOI"></a>
    </td>
  </tr>
</table>

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

## search-query

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/CoLRev-Environment/search-query/refs/heads/main/docs/source/_static/search_query_logo.svg" alt="SearchQuery Logo" width="250">
    </td>
    <td>
      <a href="https://github.com/CoLRev-Environment/search-query">
        <img src="https://img.shields.io/github/commit-activity/t/CoLRev-Environment/search-query" alt="Total commits">
      </a><br>
      <a href="https://github.com/CoLRev-Environment/search-query">
        <img src="https://img.shields.io/github/contributors-anon/CoLRev-Environment/search-query" alt="Contributors">
      </a><br>
    <a href="https://joss.theoj.org/papers/ea1fcafb8f80fa98bcbd857cf1cfada9"><img src="https://joss.theoj.org/papers/ea1fcafb8f80fa98bcbd857cf1cfada9/status.svg" alt="DOI"></a>
    </td>
  </tr>
</table>

**search-query** is a Python package for parsing, validating, simplifying, and serializing search queries for academic databases. It currently supports PubMed, EBSCOHost, and Web of Science, using a standardized JSON schema (Haddaway et al., 2022).

**Highlights:**

- Programmatic use, CLI interface, and optional integration via pre-commit hooks
- Zero dependencies: easily embeddable across environments
- Extensible parser/validator architecture
- Tested on real-world queries from [searchRxiv](https://www.searchrxiv.org/){: target="_blank"}

## BibDedupe

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/CoLRev-Environment/bib-dedupe/main/docs/figures/logo.png" alt="BibDedupe Logo" width="250">
    </td>
    <td>
    <a href="https://github.com/CoLRev-Environment/bib-dedupe">
      <img src="https://img.shields.io/github/commit-activity/t/CoLRev-Environment/bib-dedupe" alt="Total commits">
    </a><br>
    <a href="https://github.com/CoLRev-Environment/bib-dedupe">
      <img src="https://img.shields.io/github/contributors-anon/CoLRev-Environment/bib-dedupe" alt="Contributors">
    </a><br>
    <a href="https://joss.theoj.org/papers/b954027d06d602c106430e275fe72130"><img src="https://joss.theoj.org/papers/b954027d06d602c106430e275fe72130/status.svg" alt="DOI"></a>
    </td>
  </tr>
</table>
[BibDedupe](https://github.com/CoLRev-Environment/bib-dedupe){: target="_blank"} is an open-source **Python library for deduplication of bibliographic records**, tailored for literature reviews.
Unlike traditional deduplication methods, BibDedupe focuses on entity resolution, linking duplicate records instead of simply deleting them.

- **Automated Duplicate Linking with Zero False Positives**: BibDedupe automates the duplicate linking process with a focus on eliminating false positives.
- **Preprocessing Approach**: BibDedupe uses a preprocessing approach that reflects the unique error generation process in academic databases, such as author re-formatting, journal abbreviation or translations.
- **Entity Resolution**: BibDedupe does not simply delete duplicates, but it links duplicates to resolve the entity and integrates the data. This allows for validation, and undo operations.
- **Programmatic Access**: BibDedupe is designed for seamless integration into existing research workflows, providing programmatic access for easy incorporation into scripts and applications.
- **Transparent and Reproducible Rules**: BibDedupe's blocking and matching rules are transparent and easily reproducible to promote reproducibility in deduplication processes.
- **Continuous Benchmarking**: Continuous integration tests running on GitHub Actions ensure ongoing benchmarking, maintaining the library's reliability and performance across datasets.
- **Efficient and Parallel Computation**: BibDedupe implements computations efficiently and in parallel, using appropriate data structures and functions for optimal performance.

## Recommended research software

- [R: Tidyverse](https://www.tidyverse.org/){: target="_blank"}
- [rOpenSci](https://ropensci.org/){: target="_blank"}
