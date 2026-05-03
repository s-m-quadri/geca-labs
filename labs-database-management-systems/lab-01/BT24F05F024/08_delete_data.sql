-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;
DELETE FROM students
WHERE id = 2;
SELECT * FROM students;
-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!