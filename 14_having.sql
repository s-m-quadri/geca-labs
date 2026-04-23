-- Task 14: Having Clause
-- Show grades that have more than 1 student

USE school_db;

-- TODO: SELECT grade, COUNT(*) as count
-- FROM students
-- GROUP BY grade
-- HAVING count > 1;
;
-- Confirm before updating
SELECT * FROM students WHERE id = 1;
UPDATE students SET age = 16 WHERE id = 1;
SELECT * FROM students WHERE id = 1;