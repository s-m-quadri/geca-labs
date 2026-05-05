-- Task 3: Numeric — ABS and MOD
-- ABS: distance of each salary from 50000
-- MOD: emp_id modulo 3 (remainder)

USE school_db;

-- TODO: SELECT emp_id, full_name, salary,
--   ABS(salary - 50000) AS dist_from_50k,
--   MOD(emp_id, 3) AS id_mod_3
-- FROM employees;
USE school_db;
SELECT full_name, ABS(salary - 50000) AS diff_from_50k, MOD(emp_id, 3) AS id_mod3
FROM employees;