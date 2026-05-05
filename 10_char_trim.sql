USE school_db;

SELECT 
    full_name,
    phone,
    TRIM(phone) AS phone_clean
FROM employees;