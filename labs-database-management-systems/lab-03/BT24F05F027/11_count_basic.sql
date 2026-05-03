USE school_db;

-- Total employees
SELECT COUNT(*) AS total_employees 
FROM employees;

-- One query: total + high earners (salary >= 40000)
SELECT 
    COUNT(*) AS total_employees,
    SUM(CASE 
            WHEN salary >= 40000 THEN 1 
            ELSE 0 
        END) AS high_earners
FROM employees;