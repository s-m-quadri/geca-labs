-- Task 4: Date — current date and time
-- Compare hire_date to today using CURDATE() and show NOW() once.

USE school_db;

-- Show current date and time
SELECT NOW() AS server_time;

-- Compare hire_date with today's date
SELECT 
    full_name,
    hire_date,
    CURDATE() AS today,
    (CURDATE() >= hire_date) AS hired_on_or_before_today
FROM employees;

-- TODO: SELECT NOW() AS server_time;

-- TODO: SELECT full_name, hire_date, CURDATE() AS today,
--   (CURDATE() >= hire_date) AS hired_on_or_before_today
-- FROM employees;
