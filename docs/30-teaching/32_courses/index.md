---
layout: default
title: 32 Courses
parent: Teaching
has_toc: true
nav_order: 3
has_children: true
redirect_from:
  - /docs/30-teaching/30_processes/30.02.courses.html
transition_status: "toupdate"
transition_comment: "Update the course overview"
---

# 32 Courses

<table>
  <thead>
    <tr>
      <th>Semester</th>
      <th>Courses offered</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    {% for course in site.courses %}
    <tr>
      <td>{{ course.semester }}</td>
      <td><a href="{{ site.baseurl }}{{ course.url }}">{{ course.title }}</a></td>
      <td>{{ course.status }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>


[➕ lecture](../30_processes/30.10.lecture.html) [➕ project](../30_processes/30.12.projects.html) [➕ seminar](../30_processes/30.11.seminars.html)
{: .text-center }

Status

- ⟳ in-preparation
- ▶ in-progress
- 📋 grade / review / repeat exams
- ✔️ completed
