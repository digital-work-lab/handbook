---
layout: default
title: Welcome
nav_order: 1
description: "Welcome"
permalink: /
---

# The handbook

This handbook is a collaborative and participatory initiative to facilitate our research activities, and consistently deliver high-quality service to students.
It documents our processes related to 

- Section 10: [Lab management](docs/10-lab/)
- Section 20: [Research](docs/20-research/)
- Section 30: [Teaching](docs/30-teaching/)
- Section 40: [Funding](docs/40-funding)
- Section 50: [Service](docs/50-service/)

Each section has a unique number, which helps us to organize handbook documents and files on our shared [data store](docs/10-lab/10_processes/10.05.systems-overview.html#nextcloud){: target="_blank"}. For example, theses are in section [30.40](docs/30-teaching/30_processes/30.40.theses.html). 

There are external repositories for the following teaching offers:

- [digital work lecture](https://digital-work-lab.github.io/digital-work-lecture/){: target="_blank"}
- [literature review seminar](https://digital-work-lab.github.io/literature-review-seminar/){: target="_blank"}
- [open source project](https://digital-work-lab.github.io/open-source-project/){: target="_blank"}
- [theses](https://digital-work-lab.github.io/theses/){: target="_blank"}

The handbook takes inspiration from [GitLab's Handbook](https://handbook.gitlab.com/){: target="_blank"}, providing an open and transparent resource in the academic context.

## Contributing

We invite everyone to contribute to it using the [issues](https://github.com/digital-work-lab/handbook/issues){: target="_blank"} and [pull requests](https://github.com/digital-work-lab/handbook/pulls){: target="_blank"} and to use it as a resource.
Instructions and guidelines are available in [10.10 Handbook](docs/10-lab/10_processes/10.10.handbook.html).

<!--
## Recent changes

- [Handbook changes in July](https://github.com/digital-work-lab/handbook/compare/6e0b3da0c213f74dce154642892d50e5ed96a9b3...6e0b3da0c213f74dce154642892d50e5ed96a9b3)

## Contact

Offices: WE5/1.081.

[Schedule a meeting](https://calendly.com/gerit-wagner/30min){: .btn .btn-green }

<iframe width="600" height="200" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=10.862774848937988%2C49.89987300208533%2C10.876936912536623%2C49.90642391513594&amp;layer=mapnik&amp;marker=49.9031485698061%2C10.869855880737305" style="border: 1px solid black"></iframe>
-->

## Handbook contributors

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>
