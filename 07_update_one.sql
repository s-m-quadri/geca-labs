-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
USE school_db;
-- Confirm before updating
SELECT * FROM students WHERE id = 1;
UPDATE students SET age = 16 WHERE id = 1;
SELECT * FROM students WHERE id = 1;