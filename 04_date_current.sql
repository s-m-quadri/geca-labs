USE school_db;

-- Show current date and time of server
SELECT NOW() AS server_time;

-- Compare hire_date with today's date
SELECT 
    full_name, 
    hire_date, 
    CURDATE() AS today,
    (CURDATE() >= hire_date) AS hired_on_or_before_today
FROM employees;