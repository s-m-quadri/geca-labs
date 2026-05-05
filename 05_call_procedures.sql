-- Task 5: CALL apply_rate (created in task 4)
-- Run after ./run_source.sh proc_lab 04_proc_apply_rate.sql

USE proc_lab;

-- TODO: CALL apply_rate(200, 10, @out);
CALL apply_rate(200, 10, @out);
-- TODO: SELECT @out AS with_tax;
SELECT @out AS with_tax;
