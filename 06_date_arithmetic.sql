-- Task 6: Date — DATEDIFF and DATE_ADD
-- Days employed: DATEDIFF from hire_date to CURDATE()
-- One-year anniversary: DATE_ADD(hire_date, INTERVAL 1 YEAR)

USE school_db;

SELECT full_name, hire_date,
  DATEDIFF(CURDATE(), hire_date) AS days_employed
FROM employees;

SELECT full_name, hire_date,
  DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary
FROM employees;
