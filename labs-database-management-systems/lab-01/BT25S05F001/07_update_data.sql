-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;
ALTER TABLE students
MODIFY COLUMN phone VARCHAR(20);
 
DESCRIBE students;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
