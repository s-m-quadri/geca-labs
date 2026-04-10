-- Task 8: Character — CONCAT
-- Build a single label column: "Name | Dept | Salary"

USE school_db;

SELECT full_name,
  CONCAT(full_name, ' | ', dept, ' | ', salary) AS label
FROM employees;
