-- Task 12: Count — COUNT(DISTINCT)
-- How many distinct departments appear?

USE school_db;

SELECT COUNT(DISTINCT dept) AS distinct_depts FROM employees;
