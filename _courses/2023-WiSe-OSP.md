---
layout: default
title: OSP
title_long: Open-Source Projekt (WI-Projekt)
parent: 32 Courses
grand_parent: Teaching
semester: 2023-WiSe
status: ✔️
student_evaluations: "000061_20240130_WS2324_Evaluation_WI-Projekt.pdf"
improvement_issue: "https://github.com/digital-work-lab/open-source-project/issues/3"
improvement_status: ✔️
---

# OSP 2023 WiSe

Field               | Value
------------------- | -------------------------------
Title               | {{ page.title_long }}
Lecturer            | Gerit Wagner
Link: VC            | [VC](https://vc.uni-bamberg.de/course/view.php?id=64616){: target="_blank"}
Link: Website       | [Website](https://www.uni-bamberg.de/digital-work/studium/bachelor/wi-projekt-open-source-projekt/){: target="_blank"}, [open-source-development](https://digital-work-lab.github.io/open-source-project/){: target="_blank"}
Status              | {{ page.status }}
Student Evaluations | <a href="{{ site.baseurl }}/assets/evaluations/{{ page.student_evaluations }}" target="_blank">PDF</a>
Improvement Issue   | <a href="{{ page.improvement_issue }}" target="_blank">Issue Link</a>
Status of Revisions | {{ page.improvement_status }}

## Process

## 1. Announce the project (4 months before)
 
Start: December (summer term), May (winter term)

- [x] Professor: Announce project on the website for the next semester (without dates/rooms).
- [x] Secretary: Create the project in FlexNow.
- [x] Professor: Update information in UnivIS (**add keywords „WI-Projekt“ and „WI-Projekte“**), check information on the website. VC/UnivIS: "WI-Projekt-B: Bachelorprojekt aus der Fächergruppe Wirtschaftsinformatik"
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

- [x] Professor: Schedule evaluations in the pen-ultimate week ([30.21.evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [x] Scheine ([Formular](https://www.uni-bamberg.de/ism/studium/anmeldung-scheinklausur/){: target="_blank"}), Scheinklausur-anmeldungen bei Erstellung der Klausurbögen berücksichtigen

## 4. Grading and documentation

Grading

- [x] Create reminder for the deadline.
- [x] Use the [grading scripts](https://github.com/digital-work-lab/handbook/tree/main/src/grading){: target="_blank"} to assign grades and prepare FlexNow import
- [x] Have failed exams reviewed by a second professor (?)

Entering Grades into FlexNow

- [x] Secretary: Enter grades in FlexNow (or create certificates if exam is not yet available in FlexNow ([script](https://github.com/digital-work-lab/handbook/tree/main/src/scheine){: target="_blank"})).

    - [Login: FlexNow](https://fn2web.zuv.uni-bamberg.de/FN2AUTH/FN2AuthServlet?op=Login){: target="_blank"} - Lehrstuhlmodul - Prüfungsteilnehmer / zentral organisiert / Veranstaltung auswählen / Teilnehmer laden
    - Formular zum Ändern einzelner Teilnehmer: Noten eingeben (Punkte müssen nicht eingegeben werden), speichern und weiter
    - Oder CSV: export (utf-8), add grades/points via vlookup, import (csv-format: semicolon, no quotes)
        - Im oberen Bereich: Teilnehmer laden, drucken, exportieren via LV-Semester:
    "Noten endgültig freischalten und verbuchen" ([14.01](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/10-lab/14_grades/01_lectures&fileid=71){: target="_blank"}). After the activation, changes can only be made through the examination office (wiai.pruefungen@uni-bamberg.de)
    - Only store grades as PDF (not as csv)?
    - Klausuren entsprechend der Reihenfolge im PDF sortieren.

Grades are archived at [14.02](https://nc-2272638881871040784.nextcloud-ionos.com/index.php/apps/files/?dir=/10-lab/14_grades/02_projects&fileid=69){: target="_blank"}.

Sending exams to the examination office

- [x] Professor: Exams are sent to the examination office (in person): [Silke Nüßlein](https://univis.uni-bamberg.de/prg?search=persons&show=info&department=322130&fullname=Silke+Nue%C3%9Flein){: target="_blank"}, Kapuzinerstr. 25, 00.01

Documentation

- [x] Professor: Analyse the evaluations, store the files, and document the improvements (see [evaluations]({{ site.baseurl }}/docs/30-teaching/30_processes/30.21.evaluations.html)).
- [x] Professor: [Report]({{ site.baseurl }}/docs/30-teaching/30_processes/30.20.reports.html) teaching efforts at the end of the semester.
- [x] Professor: Archive presentation protocols (projects and seminars: digital is sufficient).

Deadline: End of August (summer term), March (winter term)
