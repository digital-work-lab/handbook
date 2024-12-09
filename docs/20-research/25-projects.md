---
layout: default
title: 25 Projects
parent: Research
nav_order: 6
---

# 25 Projects

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


{: .resource } 
> Confidential project data are stored here:
> 
> - [GitHub](https://github.com/orgs/digital-work-lab/repositories?q=topic%3Aresearch){: target="_blank"}
> - [Nextcloud](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/20-research/25_projects&fileid=88094){: target="_blank"}
