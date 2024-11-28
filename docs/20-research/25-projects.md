---
layout: default
title: 25 Projects
parent: Research
nav_order: 6
---

# 25 Projects
{: .d-inline-block }

<table>
  <thead>
    <tr>
      <th>Project</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    {% for project in site.projects %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td>{{ project.status }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

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

{: .confidential } 
> Confidential project data are stored here:
> 
> - [GitHub](https://github.com/orgs/digital-work-lab/repositories?q=topic%3Aresearch){: target="_blank"}
> - [Nextcloud](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/20-research/25_projects&fileid=88094){: target="_blank"}
