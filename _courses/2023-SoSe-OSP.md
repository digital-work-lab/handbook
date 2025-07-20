---
layout: default
title: OSP
title_long: Open-Source Projekt (WI-Projekt)
parent: 32 Courses
grand_parent: Teaching
semester: 2023-SuSe
status: ✔️
student_evaluations: "000033_20230723_SS23-Evaluation-Digital-Work-Projekt-B.pdf"
improvement_issue: "https://github.com/digital-work-lab/open-source-project/issues/9"
improvement_status: ✔️
---

# OSP 2023 SuSe

Field               | Value
------------------- | ------------------------------------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | [VC](https://vc.uni-bamberg.de/enrol/index.php?id=61245){: target="_blank"}
Link: Website       | [Website](https://www.uni-bamberg.de/digital-work/studium/bachelor/wi-projekt-open-source-projekt/){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | {% if page.student_evaluations != "" %} <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Improvement Issue   | {% if page.improvement_issue != "" %} <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Status of Revisions | {{ page.improvement_status }}
