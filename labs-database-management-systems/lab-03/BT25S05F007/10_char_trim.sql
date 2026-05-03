USE school_db;

-- Remove leading and trailing spaces from phone numbers
SELECT 
    full_name,
    phone,
    TRIM(phone) AS phone_clean
FROM employees;