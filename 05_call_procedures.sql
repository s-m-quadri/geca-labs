-- Task 5: Call apply_rate (created in task 4)
-- PostgreSQL functions are called with SELECT, not CALL + session variable
\c proc_lab

SELECT apply_rate(200, 10) AS with_tax;
