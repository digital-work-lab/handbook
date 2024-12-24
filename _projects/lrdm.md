---
layout: default
title: lrdm
title_long: ""
parent: 25 Projects
grand_parent: Research
started: 2022-02-20
area: knowledge_synthesis
resources: []
status: writing
improvement_status: pending
topics: ['paper', 'research']
repository_url: https://github.com/digital-work-lab/lrdm
archived: False
updated_recently: True
associated_projects: []
labot_workflow_status: success
project_type: ['paper']
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

{% if page.resources %}
## Resources

  {% for output in page.resources %}
  - [{{ output.name }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.outputs %}
## Outputs

  {% for output in page.outputs %}
  - [{{ output.type }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.related %}
## Related projects 

- {% for item in page.related %}
  - <a href="{{ item }}">{{ item }}</a>
{% endfor %}
{% endif %}