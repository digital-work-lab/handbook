---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---


# The handbook

The goal of the internal handbook is to document our processes related to research, teaching, and administration. We invite everyone to use it as a resource and to contribute to it using the [issues](https://github.com/digital-work-lab/handbook/issues) and [pull requests](https://github.com/digital-work-lab/handbook/pulls).

<!--  [Schedule a meeting](https://calendly.com/gerit-wagner/30min){: .btn .btn-green } -->

## Recent changes

- [Handbook changes in July](https://github.com/digital-work-lab/handbook/compare/6e0b3da0c213f74dce154642892d50e5ed96a9b3...6e0b3da0c213f74dce154642892d50e5ed96a9b3)

## Contributors

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>
