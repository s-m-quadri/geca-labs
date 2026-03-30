-- Task 12: Count — COUNT(DISTINCT)
-- How many distinct departments appear?

USE school_db;

-- TODO: SELECT COUNT(DISTINCT dept) AS distinct_depts FROM employees;

select count(distinct dept) as distinct_depts from employees;