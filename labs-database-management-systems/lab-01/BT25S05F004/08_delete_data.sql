-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
DELETE FROM student_info WHERE rollno=3;
SELECT * FROM student_info;