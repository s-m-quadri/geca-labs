-- Task 5: CALL apply_rate (created in task 4)
-- Run after ./run_source.sh proc_lab 04_proc_apply_rate.sql

USE proc_lab;

CALL apply_rate(200, 10, @out);
SELECT @out AS with_tax;
