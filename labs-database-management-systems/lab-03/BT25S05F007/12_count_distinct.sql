USE school_db;

-- Count distinct departments
SELECT COUNT(DISTINCT dept) AS distinct_depts
FROM employees;