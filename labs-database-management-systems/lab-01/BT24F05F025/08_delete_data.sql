-- Task 8: Delete Record
-- Delete a student from the table

USE school_db;

-- TODO: Write your DELETE command here
-- Remember to use WHERE clause!
DELETE FROM students
WHERE id = 1; -- Replace with the actual student ID you want to delete
SELECT * FROM students; -- To verify the deletion