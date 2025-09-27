---
layout: default
title: 25 Projects
parent: Research
nav_order: 6
---

# 25 Projects

[![Update Project Overview](https://github.com/digital-work-lab/handbook/actions/workflows/sync-projects.yml/badge.svg)](https://github.com/digital-work-lab/handbook/actions/workflows/sync-projects.yml){: target="_blank"} [![Create Project](https://img.shields.io/badge/Create-New%20Project-blue)]([https://github.com/organizations/digital-work-lab/repositories/new](https://github.com/digital-work-lab/handbook/tree/main/_projects){: target="_blank"}){: target="_blank"}

Project pages in this section are auto-synced from repository entries tagged
with both `research` and `paper` via [`src/sync_projects_from_repos.py`](https://github.com/digital-work-lab/handbook/blob/main/src/sync_projects_from_repos.py){: target="_blank"}.

<table>
  <thead>
    <tr>
      <th>Project</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    {% for project in site.projects %}
    {% if project.status != "published" and project.status != "revising" and project.status != "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: gray;">{{ project.status }}</td>
    </tr>
    {% endif %}
    {% endfor %}

    {% for project in site.projects %}
    {% if project.status == "revising" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: orange;"><strong>{{ project.status }}</strong></td>
    </tr>
    {% endif %}
    {% if project.status == "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: blue;">{{ project.status }}</td>
    </tr>
    {% endif %}
    {% endfor %}

    {% for project in site.projects %}
    {% if project.status == "published" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: green;">{{ project.status }}</td>
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>

{: .highlight }
> See [Project portfolio](25-projects-gantt).
