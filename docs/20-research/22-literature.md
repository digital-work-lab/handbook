---
layout: default
title: 22 Literature
parent: Research
nav_order: 3
---

# 22 Literature (shared)
{: .d-inline-block }

```mermaid
graph BT
    subgraph SharedRepository["Shared Repository"]
        direction LR
        A@{ shape: lean-r, label: "References (references.bib)" }
        B@{ shape: lean-r, label: "Literature Summaries" }
        C@{ shape: lean-r, label: "PDFs (Git-LFS)" }
    end

    subgraph LocalWorkflow["Local workflow"]
        K["Import paper in Zotero"]
        K --> L["Export to Obsidian"]
        L --> D["Create literature summary, add PDF and reference"]
    end

    subgraph OnlineWorkflow["Online workflow"]
        J["Revise files in a shared repository on GitHub (upload of PDFs is not possible)"]
    end

    J --> E
    E[Pull Request]
    D --> E
    E --> SharedRepository

    style LocalWorkflow fill:white,stroke:#333,stroke-width:3px
    style SharedRepository fill:white,stroke:#333,stroke-width:3px
    style OnlineWorkflow fill:white,stroke:#333,stroke-width:3px
```

## Shared repository

Git repository with

- References: `references.bib` in Git repository
- PDFs: Git-LFS
- Obsidian literature summaries
- If Word integration (citation plugin) is needed: Zotero (for individual projects)

## Local workflow

Zotero can be used (recommended) to facilitate the export to the repository

- Quick export - with [Zotero connector](https://chromewebstore.google.com/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc){: target="_blank"} for web exports, [Zotero integration](https://github.com/mgmeyers/obsidian-zotero-integration){: target="_blank"} and [Obsidian Web Clipper](https://obsidian.md/clipper){: target="_blank"} for web export

**TODO**

- How to export PDFs efficiently / add the record to the references
- TBD: PDF Commenting (Zotero??)

## Online workflow

- No setup is required.
- Uploading PDFs to git-lfs is not possible.

**TODO**: Create concept notes with a script (not manually with obsidian/Zotero?)

## Pull request

- Labot support is enabled for pull requests (e.g., checking consistency, updating references).

Example repository: [work_hub](https://github.com/digital-work-lab/work_hub){: target="_blank"}

**TODO**:

- **PDFs cannot be uploaded online - must use the local cli for git-lfs?!**
- Zotero vs. JabRef?
- Update repo setup: include Git-LFS
- Existing projects: Move PDFs to git repositories with Git-LFS [Nextcloud](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/22-literature/23_data&fileid=88094){: target="_blank"} in sections 25 and 36.
- TBD: CoLRev repositories (PDFs and obsidian vaults)

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; max-width:100%;">
  <iframe src="https://www.youtube-nocookie.com/embed/7zE5i0WrLko"
          frameborder="0" allowfullscreen
          style="position:absolute; top:0; left:0; width:100%; height:100%;">
  </iframe>
</div>


{: .resource } 
> - [GitHub](https://github.com/orgs/digital-work-lab/repositories?q=topic%3Aresearch){: target="_blank"}
