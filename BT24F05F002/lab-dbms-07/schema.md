# Student Management System Schema

This schema models a simple student management system for a university.

Entities:
- `department`: academic departments offering majors and courses.
- `instructor`: faculty members assigned to teach courses.
- `student`: enrolled students with majors and academic status.
- `semester`: academic terms used for enrollment tracking.
- `course`: classes offered by departments with assigned instructors.
- `enrollment`: registrations of students in courses for a semester.

Key relationships:
- Each student may major in one department.
- Each instructor belongs to a department.
- Each course belongs to a department and may have one instructor.
- Each enrollment links one student, one course, and one semester.

This design supports student transcripts, current enrollments, course listings, and department reports.
![alt text](<er_diagram.jpeg>)