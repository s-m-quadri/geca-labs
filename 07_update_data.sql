-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

UPDATE students
SET grade = 'A'
WHERE student_id = 1;
