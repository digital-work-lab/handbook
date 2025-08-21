---
layout: default
title: agenda-jour-fixe
title_long: "✅ Agenda: Jour-Fixe"
parent: 25 Projects
grand_parent: Research
visibility: Private
collaborators: ['Stella1234-design']
area: other
topics: ['agenda', 'lab-management']
html_url: https://github.com/digital-work-lab/agenda-jour-fixe
archived: False
updated_recently: True
associated_projects: []
labot_workflow_status: not-applicable
project_type: []
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Visibility          | {{ page.visibility }}
Access              | {{ page.collaborators topics | join: ", "}}
Topics              | {{ page.topics | join: ", " }}
URL                 | [https://github.com/digital-work-lab/agenda-jour-fixe](https://github.com/digital-work-lab/agenda-jour-fixe){: target="_blank"}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)](https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

{{% if page.resources %}}
## Resources

  {{% for output in page.resources %}}
  - [{{ output.name }}]({{ output.link }}){{: target="_blank"}}
  {{% endfor %}}
{{% endif %}}

{{% if page.outputs %}}
## Outputs

  {{% for output in page.outputs %}}
  - [{{ output.type }}]({{ output.link }}){{: target="_blank"}}
  {{% endfor %}}
{{% endif %}}

{{% if page.related %}}
## Related projects 

- {{% for item in page.related %}}
  - <a href="{{ item }}">{{ item }}</a>
{{% endfor %}}
{{% endif %}}
