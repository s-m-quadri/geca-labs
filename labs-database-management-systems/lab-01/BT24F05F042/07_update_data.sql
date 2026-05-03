-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
USE school_db;
UPDATE students SET grade = 'A' WHERE id = 1;
SELECT * FROM students;