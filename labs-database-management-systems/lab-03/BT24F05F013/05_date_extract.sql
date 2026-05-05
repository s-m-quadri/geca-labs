-- Task 5: Date — YEAR, MONTH, DAY
-- Extract calendar parts from hire_date.

USE school_db;

-- TODO: SELECT full_name, hire_date,
--   YEAR(hire_date) AS y,
--   MONTH(hire_date) AS m,
--   DAY(hire_date) AS d
-- FROM employees;
USE school_db;

-- Extract year, month, and day from hire_date
SELECT full_name, hire_date,
       YEAR(hire_date) AS y,
       MONTH(hire_date) AS m,
       DAY(hire_date) AS d
FROM employees;