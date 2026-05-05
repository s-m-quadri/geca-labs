-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000

USE school_db;

-- Count all rows in the table
SELECT COUNT(*) AS total_employees FROM employees;

-- One query: count rows where salary >= 40000
-- Using the SUM(CASE...) pattern is the most portable SQL method
SELECT 
    COUNT(*) AS total_employees,
    SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
FROM employees;