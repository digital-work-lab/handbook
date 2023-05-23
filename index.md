---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---


# The handbook

The goal of the internal handbook is to document our processes related to research, teaching, and administration. We invite everyone to use it as a resource and to contribute to it using the [issues] and [pull requests].


#### Contributors
<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>


----
[issues]: https://github.com/digital-work-lab/handbook/issues
[pull requests]: https://github.com/digital-work-lab/handbook/pulls

[^1]: [It can take up to 10 minutes for changes to your site to publish after you push the changes to GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site).
