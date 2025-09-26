---
layout: default
title: dpkw
title_long: "Exploring the boundaries and processes of digital platforms for knowledge work: A review of information systems research"
parent: 25 Projects
grand_parent: Research
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/platform-kwork-lr-manuscript
 - name: review
   link: https://github.com/digital-work-lab/platform-kwork-lr
output:
 - name: ""
   type: "Journal Article"
   link: https://www.sciencedirect.com/science/article/abs/pii/S096386872100041X
status: published
history:
  - date: 2019-04-02
    event: started
  - date: 2021-09-18
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
