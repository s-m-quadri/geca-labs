# Database Schema

## Tables

### students
- student_id (PK)
- name
- email

### instructors
- instructor_id (PK)
- name

### courses
- course_id (PK)
- title
- instructor_id (FK)

### enrollments
- enrollment_id (PK)
- student_id (FK)
- course_id (FK)
- enrollment_date

## Relationships

- One instructor teaches many courses (1:N)
- One student can enroll in many courses (M:N via enrollments)

## Normalization

- No repeating groups (1NF)
- No partial dependencies (2NF)
- No transitive dependencies (3NF)