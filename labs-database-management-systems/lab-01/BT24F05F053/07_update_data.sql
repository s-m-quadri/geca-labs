-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
UPDATE students
SET grade = 'B'
WHERE id = 2;
SELECT * FROM students;

