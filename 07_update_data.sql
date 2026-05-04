
ALTER TABLE students
DROP COLUMN phone;
 
DESCRIBE students;
=======
-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
UPDATE students 
SET grade = 'A' 
WHERE student_name = 'Alice Johnson';
>>>>>>> 34f8c46e (Done)
