USE school_db;

-- Build a combined label string
SELECT 
    full_name,
    CONCAT(full_name, ' | ', dept, ' | ', salary) AS label
FROM employees;
