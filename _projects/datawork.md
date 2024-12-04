---
layout: default
title: datawork
title_long: ""
parent: 25 Projects
grand_parent: Research
area: work_practices
started: 2024-01-25
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/data-work
status: concept
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
