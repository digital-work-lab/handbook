---
layout: default
title: OSP
title_long: Open-Source Projekt (WI-Projekt)
parent: 32 Courses
grand_parent: Teaching
semester: 2025-SoSe
status: ▶
student_evaluations: ""
improvement_issue: "https://github.com/digital-work-lab/open-source-project/issues/189"
improvement_status: N/A
---

# OSP 2025 SoSe

Field               | Value
------------------- | -------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | [VC](https://vc.uni-bamberg.de/course/view.php?id=71962){: target="_blank"}
Link: Website       | [Website](https://www.uni-bamberg.de/digital-work/studium/bachelor/wi-projekt-open-source-projekt/){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | {% if page.student_evaluations != "" %} <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Improvement Issue   | {% if page.improvement_issue != "" %} <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Status of Revisions | {{ page.improvement_status }}

## Process

- Grading: the team assistant registers students for the seminar, enters grades, and submits them online. Students do not need to register on FlexNow.

## 1. Announce the project (4 months before)
 
Start: December (summer term), May (winter term)

- [x] Team Assistant: Create the project in FlexNow.

{: .highlight }
>  Check public holidays
>
> Flexnow: Besonderheiten bei Ausstattung/Hinweise:
> 
> - 2h in Semesterwoche 1, Tag und Zeit egal
> - 4h in Semesterwoche 2, Freitag, Uhrzeit egal, CIP-Pool
> - 2 x 4h in Semesterwoche 3, Donnerstag und Freitag, Uhrzeit egal, CIP-Pool
> - 2h in Semesterwoche 5, Donnerstag oder Freitag, Uhrzeit egal, CIP-Pool

At the end of the semester: 

- [x] Team Assistant: Update information in UnivIS (**add keywords „WI-Projekt“ and „WI-Projekte“**), check information on the website. VC/UnivIS: "WI-Projekt-B: Bachelorprojekt aus der Fächergruppe Wirtschaftsinformatik"
- [x] Team Assistant: Announce the project on the website for the next semester (without dates/rooms).

Deadline: mid-May (summer term), December/January (winter term)

## 2. Prepare the project (1 month before)

Start: March (summer term), September (winter term)

- [x] Team Assistant and Professor: Announce dates/rooms on the websites, add to calendar.
- [x] IT department: Create the VC course, two weeks before the semester starts (automatically based on UnivIS).
- [x] Professor: The project should be announced on [Instagram](https://www.instagram.com/informatik_unibamberg/){: target="_blank"} and in the [Fachschaft WIAI newsletter](https://vc.uni-bamberg.de/course/view.php?id=284){: target="_blank"}
- [x] Professor: Create a reminder for the evaluations.
- [x] Team Assistant: Add moderator and session dates in VC.
- [x] Professor: Summarize the feedback from the last course and explain how it was addressed.
- [x] Professor: Activate course in VC (visible to students).

Deadline: April (summer term), October (winter term)

## 3. Offer the project

Start: April (summer term), October (winter term)

- [x] Team Assistant: Add the presentation (exam) dates to the department calendar
- [x] Professor: Set deadline for pull-request evaluation.
- [x] Professor: Set the date for the code review session.
- [x] Professor: Add the code review session to the [calendar](../../calendar/events.yaml)
- [x] Professor: Schedule evaluations in the pen-ultimate week ([30.21.evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [ ] Scheine ([Formular](https://www.uni-bamberg.de/ism/studium/anmeldung-scheinklausur/){: target="_blank"}), Scheinklausur-anmeldungen bei Erstellung der Klausurbögen berücksichtigen

## 4. Grading and documentation

Grading

- [x] Create reminder for the deadline.
- [x] Use the [grading scripts](https://github.com/digital-work-lab/handbook/tree/main/src/grading){: target="_blank"} to assign grades and prepare FlexNow import

Entering Grades into FlexNow

- [x] Team Assistant: [Enter grades in FlexNow](../30_processes/30.15.flexnow.html#entering-grades) (or create certificates if exam is not yet available in FlexNow ([script](https://github.com/digital-work-lab/handbook/tree/main/src/scheine){: target="_blank"})).
- [ ] Professor: Archive grades and presentation protocols (projects and seminars: digital is sufficient) at [14.02](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/10-lab/14_grades/02_projects&fileid=69){: target="_blank"}.

Documentation

- [ ] Professor: Analyse the evaluations, store the files, and document the improvements (see [evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [ ] Professor: [Report]({{ site.baseurl }}/docs/30-teaching/30_processes/30.20.reports.html) teaching efforts at the end of the semester.

Deadline: End of August (summer term), March (winter term)
