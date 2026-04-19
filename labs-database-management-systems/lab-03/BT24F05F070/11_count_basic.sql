-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000 (use SUM of a condition or subquery pattern).

USE school_db;

-- TODO: 
SELECT COUNT(*) AS total_employees 
FROM employees;

-- TODO: One query: count rows where salary >= 40000
-- Hint: 
SELECT 
    (SELECT COUNT(*) FROM employees) AS total_employees,
    (SELECT COUNT(*) FROM employees WHERE salary >= 40000) AS high_earners;
