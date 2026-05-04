
-- View data first
SELECT * FROM students;
 
-- Clear all data
TRUNCATE TABLE students;
 
-- Check if empty
SELECT * FROM students;
=======
-- Task 1: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
DELETE FROM students 
WHERE id = 3;
>>>>>>> 34f8c46e (Done)
