-- Task 6: Date — DATEDIFF and DATE_ADD
-- Days employed: DATEDIFF from hire_date to CURDATE()
-- One-year anniversary: DATE_ADD(hire_date, INTERVAL 1 YEAR)

USE school_db;

-- TODO: SELECT full_name, hire_date,
--   DATEDIFF(CURDATE(), hire_date) AS days_employed
-- FROM employees;

-- TODO: SELECT full_name, hire_date,
--   DATE_ADD(hire_date, INTERVAL 1 YEAR) AS first_anniversary
-- FROM employees;

SELECT full_name, ABS(salary - 50000) AS diff_from_50k, MOD(emp_id, 3) AS id_mod3
FROM employees;