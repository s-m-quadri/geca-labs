-- Task 8: Character — CONCAT
-- Build a single label column: "Name | Dept | Salary"

USE school_db;

-- TODO: SELECT full_name,
--   CONCAT(full_name, ' | ', dept, ' | ', salary) AS label
-- FROM employees;

USE school_db;
SELECT NOW() AS current_datetime;
SELECT full_name, hire_date, CURDATE() AS today FROM employees;