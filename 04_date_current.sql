USE school_db;

-- Current server date and time
SELECT NOW() AS server_time;

-- Compare hire date with today
SELECT 
    full_name,
    hire_date,
    CURDATE() AS today,
    (CURDATE() >= hire_date) AS hired_on_or_before_today
FROM employees;