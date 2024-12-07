---
layout: default
title: edures
title_long: ""
parent: 25 Projects
grand_parent: Research
started: 2024-10-10
area: work_practices
status: writing
improvement_status: pending
related:
 - gitintro
 - gitcollaboration
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
