---
layout: default
title: genailr
title_long: ''
parent: 25 Projects
grand_parent: Research
status: under-review
associated_projects: []
resources:
  - name: GitHub repository
    link: https://github.com/digital-work-lab/genailr
    access:
      - julianprester
    last_updated: '2025-09-26'
collaborators:
  - julianprester
  - gp
  - rl
  - rm
history:
  - date: 2023-12-10
    event: started
  - date: 2024-04-25
    event: submission
    artifact: 2024-04-25-Commentary_GenAI_Anonymous.docx
  - date: 2024-10-25
    event: decision
    artifact: 2024-10-25-JIT-Decision-revise.pdf
    decision: revise
  - date: 2024-12-03
    event: revision
    artifact: 2024-12-03-Commentary_R1_anonymous.docx
  - date: 2025-07-21
    event: revision
    artifact: 2025-07-21-revision_sheet_JIN-24-0488.R1
  - date: 2025-08-14
    event: submission
    artifact: 2025-08-14-JIN-24-0488.R2_Proof_hi.pdf
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

## Outputs

{% for output in page.outputs %}
- [{{ output.type }}]({{ output.link }}){: target="_blank"}
{% endfor %}

## Related projects 

{% for item in page.related %}
- <a href="{{ item }}">{{ item }}</a>
{% endfor %}
