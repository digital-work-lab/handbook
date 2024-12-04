---
layout: default
title: dpkw
title_long: "Exploring the boundaries and processes of digital platforms for knowledge work: A review of information systems research"
parent: 25 Projects
grand_parent: Research
area: distributed_organizing
started: 2019-04-02
completed: 2021-09-18
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/platform-kwork-lr-manuscript
output:
 - name: ""
   type: "Journal Article"
   link: https://www.sciencedirect.com/science/article/abs/pii/S096386872100041X
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

{% if page.related %}
## Related projects 

- {% for item in page.related %}
  - <a href="{{ item }}">{{ item }}</a>
{% endfor %}
{% endif %}
