-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
UPDATE students
SET grade = 'A'
WHERE id = 1; -- Replace with the actual student ID you want to update  
SELECT * FROM students; -- To verify the update