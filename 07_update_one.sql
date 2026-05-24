-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
-- Update one column
-- First, check current data
SELECT * FROM students WHERE id = 1;
 
-- Update age for student with id 1
UPDATE students
SET age = 16
WHERE id = 1;
 
-- Verify the change
SELECT * FROM students WHERE id = 1;