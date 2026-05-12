USE school_db;
SELECT NOW() AS current_datetime;
SELECT full_name, hire_date, CURDATE() AS today FROM employees;