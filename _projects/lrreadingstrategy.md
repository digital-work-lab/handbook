---
layout: default
title: lrreadingstrategy
title_long: "Heuristics for exploratory reading in literature reviews"
parent: 25 Projects
grand_parent: Research
collaborators: []
associated_projects: []
resources:
  - name: manuscript
    link: "file:///home/gerit/ownCloud/data/literature_reviews/LRReadingStrategy Paper"
output:
  - name: enlit
    type: "library"
    link: https://github.com/digital-work-lab/enlit
status: published
history:
  - date: 2017-04-22
    event: started
  - date: 2020-05-17
    event: completed
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
