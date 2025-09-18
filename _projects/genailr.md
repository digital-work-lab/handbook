---
layout: default
parent: 25 Projects
grand_parent: Research
title: genailr
collaborators: ['julianprester']
associated_projects: []
status: under-review
resources:
  - name: GitHub repository
    link: https://github.com/digital-work-lab/genailr
    # TODO : update access and last updated automatically (script)
    access: ['julianprester', 'geritwagner']
    last_updated: 2025-09-15
history:
   - date: 2024-01-22
     event: started

#   - date: 2024-01-22
#     event: draft
#     artifact: 2024-01-22-genailr-paper-jp.pdf
#     notes: Initial draft (PDF)

#   - date: 2024-04-09
#     event: manuscript
#     artifact: 2024-04-09-paper.docx
#     notes: Manuscript edit (DOCX)

#   - date: 2024-04-25
#     event: reviewer-commentary
#     artifact: 2024-04-25-Commentary_GenAI_Anonymous.docx
#     round: R0
#     notes: Anonymous commentary

#   - date: 2024-04-25
#     event: title-page
#     artifact: 2024-04-25-Title page.docx
#     round: R0

#   - date: 2024-10-25
#     event: decision
#     artifact: 2024-10-25-JIT-Decision-revise.pdf
#     decision: revise
#     venue: JIT
#     round: R1
#     notes: Editorial decision letter

#   - date: 2024-12-03
#     event: reviewer-commentary
#     artifact: 2024-12-03-Commentary_R1_anonymous.docx
#     round: R1
#     notes: Anonymous commentary (R1)

#   - date: 2024-12-03
#     event: revision-table
#     artifact: 2024-12-03-Revision table.docx
#     round: R1
#     notes: Point-by-point response table

#   - date: 2024-12-03
#     event: title-page
#     artifact: 2024-12-03-Title page_R1.docx
#     round: R1

# optional fields you might already use elsewhere:
# improvement_status:
# started:
# completed:
# outputs:
# related:
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
          {% if res.link contains "https://github.com" %}
            <div style="margin-top: .25rem;">
              <a href="https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository"
                 target="_blank" rel="noopener">
                <img src="https://img.shields.io/badge/Request-Access-blue?style=for-the-badge" alt="Request Access">
              </a>
            </div>
          {% endif %}
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
