USE school_db;

SELECT 
  full_name,
  UPPER(dept) AS dept_upper,
  LOWER(full_name) AS name_lower
FROM employees;