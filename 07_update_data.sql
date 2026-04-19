-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
-- Example: UPDATE students SET grade = 'A' WHERE name = 'student_name';

UPDATE students
SET grade = 'A'
WHERE id = 1;
 
-- View updated data
SELECT * FROM students;