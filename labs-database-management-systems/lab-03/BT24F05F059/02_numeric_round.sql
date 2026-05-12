USE school_db;
SELECT full_name, salary, ROUND(salary, 0) AS rounded, ROUND(salary, 2) AS two_dp
FROM employees;