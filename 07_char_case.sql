-- Task 7: Character — UPPER and LOWER
-- Display department in uppercase and full_name in lowercase.

USE school_db;

-- TODO: SELECT full_name,
--   UPPER(dept) AS dept_upper,
--   LOWER(full_name) AS name_lower
-- FROM employees;
USE school_db;              

-- Display department in uppercase and full_name in lowercase
SELECT 
  full_name,
  UPPER(dept) AS dept_upper,
  LOWER(full_name) AS name_lower
FROM employees;
