USE school_db;

-- TODO: SELECT full_name, hire_date,
--   YEAR(hire_date) AS y,
--   MONTH(hire_date) AS m,
--   DAY(hire_date) AS d
-- FROM employees;


SELECT full_name, hire_date, 
YEAR(hire_date) AS y,
MONTH(hire_date) AS m,
DAY(hire_date) AS d 
FROM employees;