---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---


# The handbook

The goal of the internal handbook is to document our processes related to research, teaching, and administration. We invite everyone to use it as a resource and to contribute to it using the [issues](https://github.com/digital-work-lab/handbook/issues) and [pull requests](https://github.com/digital-work-lab/handbook/pulls).


## Recent changes

- [Handbook changes in June](https://github.com/digital-work-lab/handbook/compare/bc0f46199126170a6614b5fe76e4082ee6bcd59f...0a660fc751ffe64bac94a1d1ffa5e2814ddcecd9)

## Contributors

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>
