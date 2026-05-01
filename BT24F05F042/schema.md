# Schema Design

This system manages a college database.

Tables:
- students: stores student details
- faculty: stores faculty details
- courses: courses offered, linked to faculty
- enrollments: connects students and courses

Relationships:
- One faculty teaches many courses
- Many students enroll in many courses