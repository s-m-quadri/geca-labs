# Homework Lab 7 Report

## Domain pitch
A student management system for tracking departments, instructors, students, semesters, courses, and enrollments.

## Design summary
- Normalized relations with primary keys and foreign keys.
- Students can major in a department, instructors belong to departments, and courses are tied to departments.
- Enrollment links students to courses and semesters, with grade and status tracking.

## Scripts included
- `ddl.sql`: creates the database schema.
- `seed.sql`: inserts sample departments, instructors, students, semesters, courses, and enrollments.
- `queries.sql`: example queries for student listings, course enrollments, transcripts, and department summaries.

## Notes
- The schema is implemented for MySQL using InnoDB and foreign key constraints.
- No stored procedures or triggers were added in this version.

## Testing
- The provided SQL files can be executed in order to create the schema, populate sample data, and validate queries.
