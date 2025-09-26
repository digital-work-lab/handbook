---
layout: default
title: lrnlpimpact
title_long: "A deep-learning approach for citation searches"
parent: 25 Projects
grand_parent: Research
resources:
  - name: manuscript
    link: https://github.com/digital-work-lab/lrs-impact-nlp
  - name: conference_paper
    link: https://github.com/digital-work-lab/lrs-impact-uniformity
output:
 - name: "Classifying the ideational impact of Information Systems review articles: A content-enriched deep learning approach"
   type: "Journal article"
   link: https://www.sciencedirect.com/science/article/abs/pii/S0167923620301871
 - name: deep-cenic
   type: "library"
   link: https://github.com/julianprester/deep-cenic
status: published
history:
  - date: 2016-11-27
    event: started
  - date: 2020-11-04
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
