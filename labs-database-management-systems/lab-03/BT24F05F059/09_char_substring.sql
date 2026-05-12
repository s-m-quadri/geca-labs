USE school_db;
SELECT full_name, LEFT(full_name, 3) AS first3, LENGTH(full_name) AS name_len
FROM employees;