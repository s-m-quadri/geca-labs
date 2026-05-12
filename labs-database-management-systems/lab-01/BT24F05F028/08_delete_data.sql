-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;
USE school_db;
-- Always SELECT first to confirm which rows you are deleting
SELECT * FROM students WHERE id = 3;
DELETE FROM students WHERE id = 3;
SELECT * FROM students;
-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
