-- Task 10: Character — TRIM
-- Remove leading/trailing spaces from phone (use TRIM in SELECT).

USE school_db1;

-- TODO: SELECT full_name, phone,
--   TRIM(phone) AS phone_clean
-- FROM employees;
select full_name,phone,
trim(phone) AS phone_clean
from Employees;
