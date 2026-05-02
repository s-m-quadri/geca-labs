-- Task 5: Call apply_rate (created in task 4)
-- PostgreSQL functions are called with SELECT, not CALL + session variable
\c proc_lab

USE proc_lab;

CALL apply_rate(200, 10, @out);
SELECT @out AS with_tax;
