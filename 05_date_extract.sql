-- Task 5: Date — YEAR, MONTH, DAY
-- Extract calendar parts from hire_date.

USE school_db;

-- TODO: 
SELECT full_name, hire_date,
  YEAR(hire_date) AS year,
  MONTH(hire_date) AS month,
  DAY(hire_date) AS day
FROM employees;
