-- Task 12: Count — COUNT(DISTINCT)
-- How many distinct departments appear?

USE school_db1;

-- TODO: SELECT COUNT(DISTINCT dept) AS distinct_depts FROM employees;
select count(distinct dept_name) AS distinct_department from Employees;
