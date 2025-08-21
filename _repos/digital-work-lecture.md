---
layout: default
title: digital-work-lecture
title_long: "Lecture Introduction to Digital Work"
parent: 25 Projects
grand_parent: Research
visibility: Public
collaborators: ['LaureenTh', 'k-schnickmann', 'Stella1234-design', 'Alexa-St']
area: teaching
topics: ['teaching', 'teaching-materials']
html_url: https://github.com/digital-work-lab/digital-work-lecture
archived: False
updated_recently: True
associated_projects: []
labot_workflow_status: success
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
URL                 | [https://github.com/digital-work-lab/digital-work-lecture](https://github.com/digital-work-lab/digital-work-lecture){: target="_blank"}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)](https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

{{% if page.resources and page.resources != empty %}}
## Resources

  {{% for output in page.resources %}}
  - [{{ output.name }}]({{ output.link }}){{: target="_blank"}}
  {{% endfor %}}
{{% endif %}}

{{% if page.outputs and page.outputs != empty %}}
## Outputs

  {{% for output in page.outputs %}}
  - [{{ output.type }}]({{ output.link }}){{: target="_blank"}}
  {{% endfor %}}
{{% endif %}}

{{% if page.related and page.related != empty %}}
## Related projects 

- {{% for item in page.related %}}
  - <a href="{{ item }}">{{ item }}</a>
{{% endfor %}}
{{% endif %}}
