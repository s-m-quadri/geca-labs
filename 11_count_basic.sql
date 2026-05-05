-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000 (use SUM of a condition or subquery pattern).

USE school_db;

SELECT COUNT(*) AS total_employees FROM employees;

SELECT SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
FROM employees;
