---
layout: default
title: 32 Courses
parent: Teaching
has_toc: true
nav_order: 3
has_children: true
---

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