-- Task 10: Character — TRIM
-- Remove leading/trailing spaces from phone (use TRIM in SELECT).

USE school_db;

SELECT full_name, phone,
  TRIM(phone) AS phone_clean
FROM employees;
