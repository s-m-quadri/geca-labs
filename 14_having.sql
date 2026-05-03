-- Task 14: Having Clause
-- Show grades that have more than 1 student

USE school_db;

-- TODO: SELECT grade, COUNT(*) as count
-- FROM students
-- GROUP BY grade
-- HAVING count > 1;
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade
HAVING count > 1;   