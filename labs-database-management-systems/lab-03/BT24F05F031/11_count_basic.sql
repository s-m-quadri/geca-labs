USE school_db;

-- Total number of employees
SELECT COUNT(*) AS total_employees
FROM employees;
-- Count of employees with salary >= 40000 (using SUM with CASE)
SELECT 
  COUNT(*) AS total_employees,
  SUM(CASE 
        WHEN salary >= 40000 THEN 1 
        ELSE 0 
      END) AS high_earners
FROM employees;
SELECT COUNT(*) AS high_earners
FROM (
  SELECT * 
  FROM employees
  WHERE salary >= 40000
) AS sub;