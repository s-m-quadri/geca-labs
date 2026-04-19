-- Task 10: Count Students
-- Count total number of students

USE school_db;

-- TODO: SELECT COUNT(*) as total_students FROM students;
-- First, check current data
SELECT * FROM students WHERE id = 1;
 
-- Update age for student with id 1
UPDATE students
SET age = 16
WHERE id = 1;
 
-- Verify the change
SELECT * FROM students WHERE id = 1;