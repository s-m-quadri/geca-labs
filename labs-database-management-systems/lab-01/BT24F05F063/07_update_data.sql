-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
ALTER TABLE students
DROP COLUMN phone;
 
DESCRIBE students;