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
      <th>Resources</th>
    </tr>
  </thead>
  <tbody>
    {%- comment -%} All projects except revising/under-review/published {%- endcomment -%}
    {% for project in site.projects %}
    {% if project.status != "published" and project.status != "revising" and project.status != "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: gray;">{{ project.status }}</td>
      <td>
        {% if project.resources %}
        <table class="resources">
          <thead>
            <tr>
              <th>Link</th>
              <th>Access</th>
              <th>Last updated</th>
            </tr>
          </thead>
          <tbody>
            {% for res in project.resources %}
            <tr>
              <td>
                <a href="{{ res.link }}" target="_blank" rel="noopener">
                  {{ res.name | default: res.link }}
                </a>
              </td>
              <td>
                {% if res.access %}
                  {{ res.access | join: ", " }}
                {% else %}
                  —
                {% endif %}
              </td>
              <td>{{ res.last_updated | default: "—" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% else %}—{% endif %}
      </td>
    </tr>
    {% endif %}
    {% endfor %}

    {%- comment -%} Revising {%- endcomment -%}
    {% for project in site.projects %}
    {% if project.status == "revising" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: orange;"><strong>{{ project.status }}</strong></td>
      <td>
        {% if project.resources %}
        <table class="resources">
          <thead>
            <tr>
              <th>Link</th>
              <th>Access</th>
              <th>Last updated</th>
            </tr>
          </thead>
          <tbody>
            {% for res in project.resources %}
            <tr>
              <td>
                <a href="{{ res.link }}" target="_blank" rel="noopener">
                  {{ res.name | default: res.link }}
                </a>
              </td>
              <td>
                {% if res.access %}
                  {{ res.access | join: ", " }}
                {% else %}
                  —
                {% endif %}
              </td>
              <td>{{ res.last_updated | default: "—" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% else %}—{% endif %}
      </td>
    </tr>
    {% endif %}
    {% if project.status == "under-review" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: blue;">{{ project.status }}</td>
      <td>
        {% if project.resources %}
        <table class="resources">
          <thead>
            <tr>
              <th>Link</th>
              <th>Access</th>
              <th>Last updated</th>
            </tr>
          </thead>
          <tbody>
            {% for res in project.resources %}
            <tr>
              <td>
                <a href="{{ res.link }}" target="_blank" rel="noopener">
                  {{ res.name | default: res.link }}
                </a>
              </td>
              <td>
                {% if res.access %}
                  {{ res.access | join: ", " }}
                {% else %}
                  —
                {% endif %}
              </td>
              <td>{{ res.last_updated | default: "—" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% else %}—{% endif %}
      </td>
    </tr>
    {% endif %}
    {% endfor %}

    {%- comment -%} Published {%- endcomment -%}
    {% for project in site.projects %}
    {% if project.status == "published" %}
    <tr>
      <td><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></td>
      <td style="color: green;">{{ project.status }}</td>
      <td>
        {% if project.resources %}
        <table class="resources">
          <thead>
            <tr>
              <th>Link</th>
              <th>Access</th>
              <th>Last updated</th>
            </tr>
          </thead>
          <tbody>
            {% for res in project.resources %}
            <tr>
              <td>
                <a href="{{ res.link }}" target="_blank" rel="noopener">
                  {{ res.name | default: res.link }}
                </a>
              </td>
              <td>
                {% if res.access %}
                  {{ res.access | join: ", " }}
                {% else %}
                  —
                {% endif %}
              </td>
              <td>{{ res.last_updated | default: "—" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% else %}—{% endif %}
      </td>
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
