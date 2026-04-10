-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
-- View data first
SELECT * FROM students;
 
-- Clear all data
TRUNCATE TABLE students;
 
-- Check if empty
SELECT * FROM students;