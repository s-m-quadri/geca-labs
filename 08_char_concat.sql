USE school_db;

SELECT 
    full_name,
    CONCAT(full_name, ' | ', dept, ' | ', salary) AS label
FROM employees;