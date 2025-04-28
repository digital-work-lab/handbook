---
layout: default
title: LRSem
title_long: The Literature Review Seminar
parent: 32 Courses
grand_parent: Teaching
semester: 2024-WiSe
status: ✔️
student_evaluations: "000109_20250126_WS24_25-DW-Sem-M__Literature_Review_Seminar.pdf"
improvement_issue: "https://github.com/digital-work-lab/literature-review-seminar/issues/31"
improvement_status: ▶
---

# LRSem 2024 WiSe

Field               | Value
------------------- | -------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | [VC](https://vc.uni-bamberg.de/course/view.php?id=70990){: target="_blank"}
Link: Website       | [the-literature-review-seminar](https://digital-work-lab.github.io/literature-review-seminar/){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | {% if page.student_evaluations != "" %} <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Improvement Issue   | {% if page.improvement_issue != "" %} <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a> {% else %} <span class="label label-yellow">Pending</span> {% endif %}
Status of Revisions | {{ page.improvement_status }}

## Process

**TODO**: set deadline etc.

- FlexNow: Seminars must be created for each semester (decentral exams), a seminar paper and presentation are mandatory
- Grading: the secretary registers students for the seminar, enters grades, and submits them online.

## 1. Announce the seminar (4 months before)
 
Start: December (summer term), May (winter term)

- [x] Professor: Announce seminar on the website for the next semester (without dates/rooms).
- [x] Secretary: Create the course in FlexNow.
- [x] Secretary: Update information in UnivIS (**add keywords „WI-Seminar“ and „WI-Seminare“**), check information on the website.
- Note: If the course is mentioned on the website, it should automatically be announced in the [Fachschaft WIAI newsletter](https://vc.uni-bamberg.de/course/view.php?id=284){: target="_blank"}{: target="_blank"}

Deadline: mid-May (summer term), December/January (winter term)

## 2. Prepare the seminar (1 month before)

Start: March (summer term), September (winter term)

- [x] Secretary and Professor: Set dates and request lecture rooms.
- [x] IT department: Create the VC course, two weeks before the semester starts (automatically based on UnivIS).
- [x] Professor: Create a reminder for the evaluations.
- [x] Secretary: Add moderator and session dates in VC.
- [x] Professor: Activate course in VC (visible to students).

Deadline: April (summer term), October (winter term)

## 3. Offer the seminar

Start: April (summer term), October (winter term)

- [x] Professor: Schedule evaluations in the pen-ultimate week ([30.21.evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [x] Professor: Set the date for the presentation. Add the date to the calendar.

## 4. Grading and documentation

Grading

- [x] Create reminder for the deadline.
- [x] Use the [grading scripts](https://github.com/digital-work-lab/handbook/tree/main/src/grading){: target="_blank"} to assign grades and prepare FlexNow import

Entering Grades into FlexNow

- [x] Secretary: [Enter grades in FlexNow](../30_processes/30.15.flexnow.html#entering-grades) (or create certificates if exam is not yet available in FlexNow ([script](https://github.com/digital-work-lab/handbook/tree/main/src/scheine){: target="_blank"})).
- [x] Professor: Archive grades presentation protocols (projects and seminars: digital is sufficient) at [14.03](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/10-lab/14_grades/03_seminars&fileid=72){: target="_blank"}.

Documentation

- [x] Professor: Analyse the evaluations, store the files, and document the improvements (see [evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [x] Professor: [Report]({{ site.baseurl }}/docs/30-teaching/30_processes/30.20.reports.html) teaching efforts at the end of the semester.

Deadline: End of August (summer term), March (winter term)
