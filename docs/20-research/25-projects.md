---
layout: default
title: 25 Projects
parent: Research
nav_order: 6
---

# 25 Projects

[![Update Repositories](https://github.com/digital-work-lab/handbook/actions/workflows/update_repositories.yaml/badge.svg)](https://github.com/digital-work-lab/handbook/actions/workflows/update_repositories.yaml){: target="_blank"} [![Create Repository](https://img.shields.io/badge/Create-New%20Repository-blue)](https://github.com/organizations/digital-work-lab/repositories/new){: target="_blank"}

{: .highlight }
> See [Project portfolio](25-projects-gantt).

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
    {% endif %}
    {% endfor %}

    {% for project in site.projects %}
    {% if project.status == "published" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: green;">{{ project.status }}</td>
    </tr>
    {% endif %}
    {% endif %}
    {% endfor %}
  </tbody>
</table>
