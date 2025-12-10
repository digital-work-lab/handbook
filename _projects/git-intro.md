---
layout: default
title: git-intro
title_long: ''
parent: 25 Projects
grand_parent: Research
status: published
associated_projects: []
resources:
  - name: GitHub repository
    link: https://github.com/digital-work-lab/git-intro
    access:
      - LaureenTh
    last_updated: 2025-12-10
collaborators:
  - LaureenTh
history:
  - date: 2023-04-04
    event: started
  - date: 2024-08-28
    event: completed
output:
  - name: "Rethinking How We Teach Git: Recommendations and Practical Strategies for
      the Information Systems Curriculum"
    type: "Journal Article"
    link: "https://jise.org/archives.html"
  - name: "Rethinking How We Teach Git"
    type: "Practitioner summary"
    link: "https://digital-work-lab.github.io/rethink-git-teaching/"
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Team                | {{ page.collaborators | join: ", " }}
Status              | {{ page.status }}

## Resources
{% if page.resources %}
<table class="resources">
  <thead>
    <tr>
      <th>Name</th>
      <th>Access</th>
      <th>Last updated</th>
      <th>Request</th>
    </tr>
  </thead>
  <tbody>
    {% for res in page.resources %}
    <tr>
      <td>
        {% if res.link %}
          <a href="{{ res.link }}" target="_blank" rel="noopener">
            {{ res.name | default: res.link }}
          </a>
        {% else %}
          {{ res.name | default: "—" }}
        {% endif %}
      </td>
      <td>
        {% if res.access and res.access.size > 0 %}
          {% for u in res.access %}
            {% if forloop.first == false %}, {% endif %}
            <a href="https://github.com/{{ u }}" target="_blank" rel="noopener">@{{ u }}</a>
          {% endfor %}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.last_updated %}
          {{ res.last_updated | date: "%Y-%m-%d" }}
        {% else %}
          —
        {% endif %}
      </td>
      <td>
        {% if res.link and res.link contains "https://github.com" %}
          <a href="https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository"
             target="_blank" rel="noopener">
            <img src="https://img.shields.io/badge/Request-Access-blue" alt="Request Access">
          </a>
        {% else %}
          —
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% else %}
<p>—</p>
{% endif %}
