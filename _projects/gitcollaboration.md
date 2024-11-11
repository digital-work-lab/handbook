---
layout: default
title: gitcollaboration
title_long: ""
parent: 25 Projects
grand_parent: Research
status: writing
improvement_status: pending
related:
 - gitintro
 - teapad
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
