-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
 -- Ensure the 'grade' column exists before updating
UPDATE students SET grade = 'A' WHERE student_name = 'Alic Johnson';
SELECT * FROM students; -- This line is just to verify the record update, you can remove