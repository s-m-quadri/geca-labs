USE school_db;

-- Convert department to uppercase and name to lowercase
SELECT 
    full_name,
    UPPER(dept) AS dept_upper,
    LOWER(full_name) AS name_lower
FROM employees;