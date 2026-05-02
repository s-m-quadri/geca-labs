-- Task 12: Count — COUNT(DISTINCT)
-- How many distinct departments appear?

USE school_db;

-- TODO: SELECT COUNT(DISTINCT dept) AS distinct_depts FROM employees;

USE school_db;
SELECT full_name,
       DATEDIFF(CURDATE(), hire_date)              AS days_employed,
       DATE_ADD(hire_date, INTERVAL 1 YEAR)        AS first_anniversary
FROM employees;