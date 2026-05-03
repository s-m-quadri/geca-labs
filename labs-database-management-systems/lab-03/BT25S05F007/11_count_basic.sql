USE school_db;

-- Total number of employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Count employees with salary >= 40000
SELECT 
    SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
FROM employees;