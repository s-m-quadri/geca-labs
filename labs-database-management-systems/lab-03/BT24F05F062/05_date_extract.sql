-- Task 5: Date — YEAR, MONTH, DAY
-- Extract calendar parts from hire_date.

USE school_db;

SELECT full_name, hire_date,
  YEAR(hire_date) AS y,
  MONTH(hire_date) AS m,
  DAY(hire_date) AS d
FROM employees;


USE school_db;

-- Show current server date and time
SELECT NOW() AS server_time;

-- Compare hire_date with today's date
SELECT 
    full_name, 
    hire_date, 
    CURDATE() AS today,
    (CURDATE() >= hire_date) AS hired_on_or_before_today
FROM employees;