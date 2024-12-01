---
layout: default
title: Teaching
has_children: true
has_toc: true
nav_order: 30
---

# Teaching

Our teaching activities include lectures, projects, and seminars, which are based on the following process:

{: .text-center}
```mermaid
flowchart
    subgraph Theses["Theses"]
        direction TB
        Announced(["<a href='#announced'>Announced</a>"]) --> Registered(["<a href='#registered'>Registered</a>"])
        Registered --> Submitted(["<a href='#submitted'>Submitted</a>"])
        Submitted --> Archived(["<a href='#archived'>Archived</a>"])
    end
    subgraph Courses["Courses (<a href='32_courses'>overview</a>)"]
        direction TB
        InPreparation(["<a href='#in-preparation'>In preparation</a>"]) --> InProgress(["<a href='#in-progress'>In progress</a>"])
        InProgress --> GradeReviewRepeat(["<a href='#grade-review-repeat'>Grade, review, repeat</a>"])
        GradeReviewRepeat --> Completed(["<a href='#completed'>Completed</a>"])
    end
    style Theses fill:white,stroke:#333,stroke-width:3px
    style Courses fill:white,stroke:#333,stroke-width:3px
```

## Courses

[Overview](30_processes/30.02.courses.html)

### In preparation

- [FlexNow](30_processes/30.15.flexnow.html) to [create a new module](30_processes/30.09.new_modules.html)
- [UnivIS](30_processes/30.16.univis.html) to announce courses

### In progress

- [VC](30_processes/30.19.virtual_campus.html) for student communication
- [Pedagogy](30_processes/30.07.pedagogy.html) <a href='.{{ site.baseurl }}/docs/00.goals.html'>🛠️</a>
- [Evaluations](30_processes/30.21.evaluations.html)

### Grade, review, repeat

- [Exams, repeat exams](30_processes/30.59.exams.html)
- [FlexNow](30_processes/30.15.flexnow.html) to enter grades
- [Report](30_processes/30.20.reports.html)
- [Reviews](30_processes/30.60.reviews.html)
- [Certificates](30_processes/30.51.certificates.html)
- [Improvements](30_processes/30.22.improvements.html) "<a href='.{{ site.baseurl }}/docs/00.goals.html'>♻️</a> 

### Completed

## Theses

[Thesis page](https://digital-work-lab.github.io/theses/)

{: .highlight }
> **TODO**: private thesis page

### Announced

- [Registration](30_processes/30.40.theses.html#registration)

### Registered

- [Advising](30_processes/30.40.theses.html#advising)

### Submitted

- [Grading](30_processes/30.40.theses.html#grading)
- [Feedback](https://digital-work-lab.github.io/theses/docs/feedback.html)
- [Improvement](30_processes/30.22.improvements.html) "<a href='.{{ site.baseurl }}/docs/00.goals.html'>♻️</a> 

### Archived
