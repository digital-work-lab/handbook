---
layout: default
title: OSP
title_long: Open-Source Projekt (WI-Projekt)
parent: 32 Courses
grand_parent: Teaching
semester: 2024-WiSe
status: ▶
student_evaluations: ""
improvement_issue: "https://github.com/digital-work-lab/open-source-project/issues/10"
improvement_status: ▶
---

# OSP 2024 WiSe

Field               | Value
------------------- | -------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | [VC](https://vc.uni-bamberg.de/course/view.php?id=70989){: target="_blank"}
Link: Website       | [open-source-development](https://github.com/digital-work-lab/open-source-development){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | {% if page.student_evaluations != "" %} <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a> {% else %} N/A {% endif %}
Improvement Issue   | {% if page.improvement_issue != "" %} <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a> {% else %} N/A {% endif %}

## Process

**TODO**: set deadline etc.

## 1. Announce the project (4 months before)
 
Start: December (summer term), May (winter term)

- [x] Professor: Announce project on the website for the next semester (without dates/rooms).
- [x] Secretary: Create the project in FlexNow.
- [x] Secretary: Update information in UnivIS (**add keywords „WI-Projekt“ and „WI-Projekte“**), check information on the website. VC/UnivIS: "WI-Projekt-B: Bachelorprojekt aus der Fächergruppe Wirtschaftsinformatik"
- [x] Professor: The project should be announced in the [Fachschaft WIAI newsletter](https://vc.uni-bamberg.de/course/view.php?id=284){: target="_blank"}

Deadline: mid-May (summer term), December/January (winter term)

## 2. Prepare the project (1 month before)

Start: March (summer term), September (winter term)

- [x] Secretary and Professor: Set dates and request lecture rooms.
- [x] IT department: Create the VC course, two weeks before the semester starts (automatically based on UnivIS).
- [x] Professor: Create a reminder for the evaluations.
- [x] Secretary: Add moderator and session dates in VC.
- [x] Professor: Activate course in VC (visible to students).

Deadline: April (summer term), October (winter term)

## 3. Offer the project

Start: April (summer term), October (winter term)

- [ ] Professor: Schedule evaluations in the pen-ultimate week ([30.21.evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [ ] Professor (Secretary): Prepare the exams (Deadline: day of the exam), information is typically provided one month before the semester ends (E-Mail: "Prüferbestellung"). Check whether points add up, whether the number of points per task is consistent with the grading expectations - e.g., "list two examples" should correspond to 2 or 4 points. (**TODO: where to store the exam**). Review the exam for typos. Print it and prepare the exam materials. Add the date of the exam to the calendar and prepare to hand it over personally.
- [ ] Scheine ([Formular](https://www.uni-bamberg.de/ism/studium/anmeldung-scheinklausur/){: target="_blank"}), Scheinklausur-anmeldungen bei Erstellung der Klausurbögen berücksichtigen

## 4. Grading and documentation

Grading

- [ ] Create reminder for the deadline.
- [ ] Use the [grading scripts](https://github.com/digital-work-lab/handbook/tree/main/src/grading){: target="_blank"} to assign grades and prepare FlexNow import
- [ ] Have failed exams reviewed by a second professor (?)

Entering Grades into FlexNow

- [ ] Secretary: [Enter grades in FlexNow](../30_processes/30.15.flexnow.html#entering-grades) (or create certificates if exam is not yet available in FlexNow ([script](https://github.com/digital-work-lab/handbook/tree/main/src/scheine){: target="_blank"})).
- [ ] Professor: Archive grades and presentation protocols (projects and seminars: digital is sufficient) at [14.02](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/10-lab/14_grades/02_projects&fileid=69){: target="_blank"}.

Sending exams to the examination office

- [ ] Professor: Exams are sent to the examination office (in person): [Silke Nüßlein](https://univis.uni-bamberg.de/prg?search=persons&show=info&department=322130&fullname=Silke+Nue%C3%9Flein){: target="_blank"}, Kapuzinerstr. 25, 00.01

Documentation

- [ ] Professor: Analyse the evaluations, store the files, and document the improvements (see [evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [ ] Professor: [Report]({{ site.baseurl }}/docs/30-teaching/30_processes/30.20.reports.html) teaching efforts at the end of the semester.

Deadline: End of August (summer term), March (winter term)
