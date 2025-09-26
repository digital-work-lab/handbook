---
layout: default
title: lrtracker
title_long: "Meta-analysis of Fitbit effectiveness"
parent: 25 Projects
grand_parent: Research
resources:
  - name: manuscript
    link: "file:///home/gerit/ownCloud/data/archive/2022-LRTracker Paper"
output:
 - name: "Fitbit-Based Interventions for Healthy Lifestyle Outcomes: Systematic Review and Meta-Analysis"
   type: "Journal article"
   link: https://www.jmir.org/2020/10/e23954/
status: published
history:
  - date: 2018-07-12
    event: started
  - date: 2020-10-12
    event: completed
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
