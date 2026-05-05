USE school_db;

SELECT 
    full_name,
    salary,
    ROUND(salary, 0) AS salary_whole,
    ROUND(salary, 2) AS salary_two_dec
FROM employees;