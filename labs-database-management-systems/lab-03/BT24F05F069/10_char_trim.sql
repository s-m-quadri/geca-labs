-- Task 10: Character — TRIM
-- Remove leading/trailing spaces from phone (use TRIM in SELECT).

USE school_db;

-- TODO: SELECT full_name, phone,
--   TRIM(phone) AS phone_clean
-- FROM employees;
SELECT 
    full_name, 
    phone AS phone_raw,
    TRIM(phone) AS phone_clean,
    LENGTH(phone) AS old_len,
    LENGTH(TRIM(phone)) AS new_len
FROM employees;