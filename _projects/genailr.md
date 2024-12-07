---
layout: default
title: genailr
title_long: "Generative Artificial Intelligence for Literature Reviews"
parent: 25 Projects
grand_parent: Research
area: knowledge_synthesis
started: 2023-12-10
status: under-review
improvement_status: pending
related:
  - ailr
---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}

{% if page.related %}
## Related projects 

- {% for item in page.related %}
  - <a href="{{ item }}">{{ item }}</a>
{% endfor %}
{% endif %}
