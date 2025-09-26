# School-Timetabler

A school administrator told me it currently takes around two weeks to manually build a timetable for a school of only around 20 students. Their method relied on trial and error.

This project explores whether a better approach is possible. By modeling the problem as a Constraint Satisfaction Problem (CSP), we can automatically generate a clash-free timetable.

The system takes into account:

- Which rooms support which subjects

- What classes exist and how many times per week they meet

- Which teachers teach each subject, and on which days they are available

Using a backtracking CSP solver, the program will produce a valid timetable without conflicts.

Future development will involve a web-based UI, with the program as an API call, so that the administrator can use the project in the next school year. 