-- Task 5: Date — YEAR, MONTH, DAY
-- Extract calendar parts from hire_date.

USE school_db;

SELECT full_name, hire_date,
  YEAR(hire_date) AS y,
  MONTH(hire_date) AS m,
  DAY(hire_date) AS d
FROM employees;
