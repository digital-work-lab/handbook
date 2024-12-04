---
layout: default
title: colrev
title_long: "An open-source environment for collaborative reviews"
parent: 25 Projects
grand_parent: Research
area: knowledge_synthesis
started: 2021-04-15
resources:
 - name: library
   link: https://github.com/CoLRev-Environment/colrev
 - name: manuscript
   link: https://github.com/digital-work-lab/colrev-manuscript
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
