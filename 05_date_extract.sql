USE school_db;

-- Extract year, month, and day from hire_date
SELECT 
    full_name,
    hire_date,
    YEAR(hire_date) AS y,
    MONTH(hire_date) AS m,
    DAY(hire_date) AS d
FROM employees;
