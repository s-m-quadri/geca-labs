USE school_db;

-- TODO: SELECT full_name, phone,
--   TRIM(phone) AS phone_clean
-- FROM employees;

SELECT full_name, phone,
TRIM(phone) AS phone_clean
FROM employees;
