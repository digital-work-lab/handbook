---
layout: default
title: git-bot
parent: 25 Projects
grand_parent: Research
visibility: Private
collaborators: ['k-schnickmann', 'Alexa-St']
area: research
topics: ['paper', 'research']
html_url: https://github.com/digital-work-lab/git-bot
archived: False
updated_recently: True
associated_projects: []
labot_workflow_status: failure
project_type: ['paper']
started: 2025-01-15
research_area: work_practices|distributed_organizing|knowledge_synthesis
resources: []
status: writing
improvement_status: pending
repository_url: https://github.com/digital-work-lab/git-bot
---

---

# {{ page.title }}

Field               | Value
------------------- | ----------------------------------
Acronym             | {{ page.title }}
Title               | {{ page.title_long }}
Visibility          | {{ page.visibility }}
Access              | {{ page.collaborators topics | join: ", "}}
Topics              | {{ page.topics | join: ", " }}
URL                 | [https://github.com/digital-work-lab/git-bot](https://github.com/digital-work-lab/git-bot){: target="_blank"}
Status              | {{ page.status }}
Improvement         | {{ page.improvement_status }}
Started             | {{ page.started }}
Completed           | {{ page.completed }}

[![Request Access](https://img.shields.io/badge/Request-Access-blue?style=for-the-badge)](https://github.com/digital-work-lab/handbook/issues/new?assignees=geritwagner&labels=access+request&template=request-repo-access.md&title=%5BAccess+Request%5D+Request+for+access+to+repository)

## Resources

{% for output in page.resources %}
- [{{ output.name }}]({{ output.link }}){: target="_blank"}
{% endfor %}
## Outputs

{% for output in page.outputs %}
- [{{ output.type }}]({{ output.link }}){: target="_blank"}
{% endfor %}
## Related projects 

{% for item in page.related %}
- <a href="{{ item }}">{{ item }}</a>
{% endfor %}
