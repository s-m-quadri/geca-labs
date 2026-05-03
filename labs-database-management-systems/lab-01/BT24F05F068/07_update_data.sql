-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!

UPDATE students SET grade = 'A' WHERE first_name = 'John' AND last_name = 'Doe';
