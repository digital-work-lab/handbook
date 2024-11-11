---
layout: default
title: OSP
title_long: Open-Source Projekt (WI-Projekt)
parent: 32 Courses
grand_parent: Teaching
semester: 2025-SoSe
status: ⟳
student_evaluations: ""
improvement_issue: ""
improvement_status: N/A
---

# OSP 2025 SoSe

Field               | Value
------------------- | -------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | TODO
Link: Website       | [Website](https://www.uni-bamberg.de/digital-work/studium/bachelor/wi-projekt-open-source-projekt/){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | {% if page.student_evaluations != "" %} <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a> {% else %} <span class="label label-yellow">TODO</span> {% endif %}
Improvement Issue   | {% if page.improvement_issue != "" %} <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a> {% else %} <span class="label label-yellow">TODO</span> {% endif %}
Status of Revisions | {{ page.improvement_status }}

## Process

**TODO**: set deadline etc.

## 1. Announce the project (4 months before)
 
Start: December (summer term), May (winter term)

- [x] Secretary: Create the project in FlexNow.

{: .highlight }
>  Check public holidays
>
> Flexnow: Besonderheiten bei Ausstattung/Hinweise:
> 
> - 2h in KW 17 (23.04.-25.04.) Tag und Zeit egal
> - 4h in KW 18, (28.04.-02.05.) Freitag, Uhrzeit egal, CIP-Pool
> - 2 x 4h in KW 19 (05.05.-09.05.), Donnerstag und Freitag, Uhrzeit egal, CIP-Pool
> - 2h in KW 21 (19.05.-23.05.), Donnerstag oder Freitag, Uhrzeit egal, CIP-Pool

At the end of the semester: 

- [ ] Secretary: Update information in UnivIS (**add keywords „WI-Projekt“ and „WI-Projekte“**), check information on the website. VC/UnivIS: "WI-Projekt-B: Bachelorprojekt aus der Fächergruppe Wirtschaftsinformatik"
- [ ] Secretary: Announce the project on the website for the next semester (without dates/rooms).
- [ ] Professor: The project should be announced in the [Fachschaft WIAI newsletter](https://vc.uni-bamberg.de/course/view.php?id=284){: target="_blank"}

Deadline: mid-May (summer term), December/January (winter term)

## 2. Prepare the project (1 month before)

Start: March (summer term), September (winter term)

- [ ] Secretary and Professor: Announce dates/rooms on the websites, add to calendar.
- [ ] IT department: Create the VC course, two weeks before the semester starts (automatically based on UnivIS).
- [ ] Professor: Create a reminder for the evaluations.
- [ ] Secretary: Add moderator and session dates in VC.
- [ ] Professor: Activate course in VC (visible to students).

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
