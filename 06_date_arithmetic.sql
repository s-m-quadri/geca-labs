USE school_db;

SELECT 
    full_name,
    hire_date,
    DATEDIFF(CURDATE(), hire_date) AS days_employed
FROM employees;

SELECT 
    full_name,
    hire_date,
    DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary
FROM employees;