-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000 (use SUM of a condition or subquery pattern).
USE school_db;

SELECT 
    COUNT(*) AS total_employees,
    SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
FROM employees;

-- TODO: One query: count rows where salary >= 40000
-- Hint: SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
--   or COUNT with WHERE in a subquery
