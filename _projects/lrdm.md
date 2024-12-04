---
layout: default
title: lrdm
title_long: ""
parent: 25 Projects
grand_parent: Research
started: 2022-02-20
area: knowledge_synthesis
resources:
 - name: library
   link: https://github.com/digital-work-lab/lr-dm
status: writing
improvement_status: pending
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
