---
layout: default
title: lrdm
title_long: "Artificial intelligence and the conduct of literature reviews"
parent: 25 Projects
grand_parent: Research
started: 2022-02-20
resources:
 - name: library
   link: https://github.com/digital-work-lab/lr-dm
output:
 - name: "Artificial intelligence and the conduct of literature reviews"
   type: "Journal Article"
   link: "https://journals.sagepub.com/doi/abs/10.1177/02683962211048201"
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
