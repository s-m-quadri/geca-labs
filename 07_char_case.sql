-- Select the database
USE school_db;

-- Run the query
SELECT 
    full_name,
    UPPER(dept) AS dept_upper,
    LOWER(full_name) AS name_lower
FROM employees;