---
layout: default
title: olmcareers
title_long: ""
parent: 25 Projects
started: 2023-05-04
area: distributed_organizing
grand_parent: Research
resources:
 - name: manuscript
   link: https://github.com/julianprester/dpkw-signalling
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
