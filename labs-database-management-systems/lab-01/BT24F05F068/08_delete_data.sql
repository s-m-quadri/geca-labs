-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!

DELETE FROM students WHERE first_name = 'Emily' AND last_name = 'Johnson';
