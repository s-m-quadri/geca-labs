-- Task 8: Character — CONCAT
-- Build a single label column: "Name | Dept | Salary"

USE school_db1;

-- TODO: SELECT full_name,
--   CONCAT(full_name, ' | ', dept, ' | ', salary) AS label
-- FROM employees;
select full_name,
concat(full_name,' ** ',dept_name,' ** ',salary) AS label
FROM Employees;