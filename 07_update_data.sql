-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

UPDATE students
SET grade = 'A'
WHERE student_name = 'Aarav Patel';

SELECT student_name, grade FROM students WHERE student_name = 'Aarav Patel';
