---
layout: default
title: ailr
title_long: "Artificial intelligence and the conduct of literature reviews"
parent: 25 Projects
grand_parent: Research
area: knowledge_synthesis
started: 2020-11-26
completed: 2021-09-02
resources:
 - name: library
   link: https://github.com/digital-work-lab/lr-dm
output:
 - name: "Artificial intelligence and the conduct of literature reviews"
   type: "Journal Article"
   link: "https://journals.sagepub.com/doi/abs/10.1177/02683962211048201"
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
Started             | {{ page.started }}
Completed           | {{ page.completed }}

{% if page.resources %}
## Resources

  {% for output in page.resources %}
  - [{{ output.name }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.outputs %}
## Outputs

  {% for output in page.outputs %}
  - [{{ output.type }}]({{ output.link }}){: target="_blank"}
  {% endfor %}
{% endif %}

{% if page.related %}
## Related projects 

- {% for item in page.related %}
  - <a href="{{ item }}">{{ item }}</a>
{% endfor %}
{% endif %}
