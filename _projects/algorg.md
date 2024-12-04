---
layout: default
title: algorg
title_long: ""
parent: 25 Projects
grand_parent: Research
area: distributed_organizing
started: 2024-08-14
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/alg-org
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
