---
layout: default
title: lrreadingstrategy
title_long: "Heuristics for exploratory reading in literature reviews"
parent: 25 Projects
grand_parent: Research
started: 2017-04-22
completed: 2020-05-17
area: knowledge_synthesis
output:
 - name: enlit
   type: "library"
   link: https://github.com/digital-work-lab/enlit
status: published
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
