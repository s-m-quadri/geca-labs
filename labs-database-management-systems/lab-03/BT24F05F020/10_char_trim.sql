-- Task 10: Character — TRIM
-- Remove leading/trailing spaces from phone (use TRIM in SELECT).

USE school_db;

-- TODO: SELECT full_name, phone,
--   TRIM(phone) AS phone_clean
-- FROM employees;

UPDATE employees
SET phone = CASE
    WHEN full_name = 'Meeran Shaikh' THEN ' 9838495802'
    WHEN full_name = 'Krutarth Fulare' THEN '9123456780'
    WHEN full_name = 'Prabhat Jha' THEN ' 9988776655'
    WHEN full_name = 'Tanmay Kolhe' THEN '8877665544 '
    WHEN full_name = 'Sarthak Deshmukh' THEN '9012345678'
END;

SELECT full_name, phone,
    TRIM(phone) AS phone_clean
FROM employees;