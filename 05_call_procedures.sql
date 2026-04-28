-- Task 5: CALL apply_rate (created in task 4)
-- Run after ./run_source.sh proc_lab 04_proc_apply_rate.sql

CALL apply_rate(200, 10, @with_tax);
SELECT @with_tax AS with_tax;
