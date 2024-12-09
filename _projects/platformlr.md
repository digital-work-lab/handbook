---
layout: default
title: platformlr
title_long: "A Framework of Platform Design Mechanisms, Platform Congruence and Value Creation on C2C Platforms"
parent: 25 Projects
grand_parent: Research
area: distributed_organizing
started: 2019-03-28
completed: 2021-11-22
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/platform-lr-manuscript
 - name: review
   link: https://github.com/digital-work-lab/platform-lr
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
