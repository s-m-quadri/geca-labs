USE school_db;

-- Calculate number of days employed
SELECT 
    full_name, 
    hire_date,
    DATEDIFF(CURDATE(), hire_date) AS days_employed
FROM employees;

-- Calculate first anniversary (1 year after hire_date)
SELECT 
    full_name, 
    hire_date,
    DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary
FROM employees;