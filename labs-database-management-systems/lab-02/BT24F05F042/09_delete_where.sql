-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;

-- TODO: First, see who will be deleted
-- SELECT * FROM students WHERE age < 15;

-- TODO: Then delete them
-- DELETE FROM students WHERE age < 15;

-- TODO: Check result
-- SELECT * FROM students;
-- Total students
SELECT COUNT(*) as total_students FROM students;
 
-- Average age
SELECT AVG(age) as average_age FROM students;
 
-- Oldest and youngest
SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
 
-- Count by grade
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade;
