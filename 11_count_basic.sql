-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000 (use SUM of a condition or subquery pattern).

USE school_db;

-- TODO: SELECT COUNT(*) AS total_employees FROM employees;
SELECT COUNT(*) AS total_employees FROM employees;

-- TODO: One query: count rows where salary >= 40000
-- Hint: SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
--   or COUNT with WHERE in a subquery  
SELECT SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners     
FROM employees;
