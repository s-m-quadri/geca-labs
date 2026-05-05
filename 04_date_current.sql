-- Task 4: Date — current date and time
-- Compare hire_date to today using CURDATE() and show NOW() once.

USE school_db;

-- Display the current server timestamp
SELECT NOW() AS server_time;

-- Compare employee hire dates with the current date
SELECT 
    full_name, 
    hire_date, 
    CURDATE() AS today,
    (CURDATE() >= hire_date) AS hired_on_or_before_today
FROM employees;