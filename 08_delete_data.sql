-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
DELETE FROM students WHERE student_name = 'Charlie Brwn';
SELECT * FROM students; -- This line is just to verify the record deletion, you can remove