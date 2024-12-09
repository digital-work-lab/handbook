---
layout: default
parent: 25 Projects
grand_parent: Research
area: distributed_organizing
started: 2023-04-04
completed: 2024-08-28
title: gitintro
title_long: "Rethinking How We Teach Git: Recommendations and Practical Strategies for the Information Systems Curriculum"
status: published
improvement_status: completed
resources:
 - name: manuscript
   link: https://github.com/digital-work-lab/git-intro
related:
 - gitcollaboration
 - teapad
output:
  - name: "Rethinking How We Teach Git: Recommendations and Practical Strategies for the Information Systems Curriculum"
    type: "Journal Article"
    link: "https://jise.org/archives.html"
  - name: "Rethinking How We Teach Git"
    type: "Practitioner summary"
    link: "https://digital-work-lab.github.io/rethink-git-teaching/"
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
