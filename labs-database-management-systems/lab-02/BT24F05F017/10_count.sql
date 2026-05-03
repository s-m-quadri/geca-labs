-- Task 10: Count Students
-- Count total number of students

USE school_db;

-- TODO: SELECT COUNT(*) as total_students FROM students;
-- First, see who will be deleted
SELECT * FROM students
WHERE age < 15;

-- Then delete them
DELETE FROM students
WHERE age < 15;

-- Check result
SELECT * FROM students;