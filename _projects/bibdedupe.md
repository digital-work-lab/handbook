---
layout: default
title: bibdedupe
title_long: "Python library for deduplication of bibliographic records"
parent: 25 Projects
grand_parent: Research
area: knowledge_synthesis
started: 2023-11-11
resources:
 - name: library
   link: https://github.com/CoLRev-Environment/bib-dedupe
output:
 - name: ""
   type: "Journal article"
   link: https://joss.theoj.org/papers/10.21105/joss.06318
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

{% if page.outputs %}
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
