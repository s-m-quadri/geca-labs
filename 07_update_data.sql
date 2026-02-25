-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
SELECT * FROM students;
-- UPDATE students SET grade ='A' WHERE ID = 1;
UPDATE students SET grade ='A' WHERE ID = 2;
UPDATE students SET grade ='A' WHERE ID = 3;