---
layout: default
parent: 25 Projects
grand_parent: Research
title: genailr
title_long: ""
collaborators: ['julianprester']
associated_projects: []
status: under-review
resources:
  - name: GitHub repository
    link: https://github.com/digital-work-lab/genailr
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
Title               | {{ page.title_long }}
Access              | {{ page.collaborators | join: ", " }}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)](https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

## Resources

{% for output in page.resources %}
- [{{ output.name }}]({{ output.link }}){: target="_blank"}
{% endfor %}

## Outputs

{% for output in page.outputs %}
- [{{ output.type }}]({{ output.link }}){: target="_blank"}
{% endfor %}

## Related projects 

{% for item in page.related %}
- <a href="{{ item }}">{{ item }}</a>
{% endfor %}
