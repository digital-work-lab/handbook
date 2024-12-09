---
layout: default
parent: 25 Projects
grand_parent: Research
started: 2021-02-03
completed: 2023-06-10
area: work_practices
title: healthcareai
title_long: "An Overview of AI Maturity in Health Care across 10 OECD Countries"
resources:
  - name: manuscript
    link: file:///home/gerit/ownCloud/data/health/HealthCareAI
status: published
improvement_status: completed
output:
  - name: "AI maturity in health care: An overview of 10 OECD countries"
    type: "Journal Article"
    link: "https://www.sciencedirect.com/science/article/abs/pii/S0168851023002233"
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

