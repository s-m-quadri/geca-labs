USE school_db;

-- Days employed (difference between today and hire date)
SELECT 
    full_name,
    hire_date,
    DATEDIFF(CURDATE(), hire_date) AS days_employed
FROM employees;

-- First anniversary date (1 year after hire date)
SELECT 
    full_name,
    hire_date,
    DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary
FROM employees;