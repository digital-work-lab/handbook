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
    {% for repo in site.repos %}
    {% if repo.topics contains "paper" %}
    {% if repo.status != "published" and repo.status != "revising" and repo.status != "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ repo.url }}">{{ repo.title }}</a></td>
      <td style="color: gray;">{{ repo.status }}</td>
    </tr>
    {% endif %}
    {% endif %}
    {% endfor %}

    {% for repo in site.repos %}
    {% if repo.topics contains "paper" %}
    {% if repo.status == "revising" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ repo.url }}">{{ repo.title }}</a></td>
      <td style="color: orange;"><strong>{{ repo.status }}</strong></td>
    </tr>
    {% endif %}
    {% if repo.status == "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ repo.url }}">{{ repo.title }}</a></td>
      <td style="color: blue;">{{ repo.status }}</td>
    </tr>
    {% endif %}
    {% endif %}
    {% endfor %}

    {% for repo in site.repos %}
    {% if repo.topics contains "paper" %}
    {% if repo.status == "published" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ repo.url }}">{{ repo.title }}</a></td>
      <td style="color: green;">{{ repo.status }}</td>
    </tr>
    {% endif %}
    {% endif %}
    {% endfor %}
  </tbody>
</table>
