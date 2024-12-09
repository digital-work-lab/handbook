---
layout: default
title: lrreadingstrategy
title_long: "Heuristics for exploratory reading in literature reviews"
parent: 25 Projects
grand_parent: Research
started: 2017-04-22
completed: 2020-05-17
area: knowledge_synthesis
resources:
  - name: manuscript
    link: "file:///home/gerit/ownCloud/data/literature_reviews/LRReadingStrategy Paper"
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
