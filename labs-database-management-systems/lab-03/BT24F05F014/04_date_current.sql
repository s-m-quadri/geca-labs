-- Task 4: Date — current date and time
-- Compare hire_date to today using CURDATE() and show NOW() once.

USE school_db;

-- TODO: SELECT NOW() AS server_time;

-- TODO: SELECT full_name, hire_date, CURDATE() AS today,
--   (CURDATE() >= hire_date) AS hired_on_or_before_today
-- FROM employees;
USE school_db;
SELECT NOW() AS current_datetime;
SELECT full_name, hire_date, CURDATE() AS today FROM employees;