-- Task 14: Having Clause
-- Show grades that have more than 1 student

USE school_db;
select grade, count(*) as count from students group by grade having count > 1;


-- TODO: SELECT grade, COUNT(*) as count
-- FROM students
-- GROUP BY grade
-- HAVING count > 1;
