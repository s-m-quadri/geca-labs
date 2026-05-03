-- Task 7: Character — UPPER and LOWER
-- Display department in uppercase and full_name in lowercase.

USE school_db1;

-- TODO: SELECT full_name,
--   UPPER(dept) AS dept_upper,
--   LOWER(full_name) AS name_lower
-- FROM employees;
select full_name,
UPPER(full_name) as captialise_name,
LOWER(dept_name) AS DEPT_LOWER
FROM Employees;