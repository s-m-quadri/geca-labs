-- Task 4: Date — current date and time
-- Compare hire_date to today using CURDATE() and show NOW() once.

USE school_db;

-- TODO: SELECT NOW() AS server_time;

-- TODO: SELECT full_name, hire_date, CURDATE() AS today,
--   (CURDATE() >= hire_date) AS hired_on_or_before_today
-- FROM employees;

SELECT NOW() AS server_time;
SELECT full_name , hire_date, CURDATE() AS today, 
(CURDATE()>=hire_date) as hired_on_or_before_today
FROM employees;