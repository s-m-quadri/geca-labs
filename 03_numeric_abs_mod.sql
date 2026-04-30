USE school_db;

-- ABS: distance from 50000, MOD: remainder of emp_id / 3
SELECT 
    emp_id,
    full_name,
    salary,
    ABS(salary - 50000) AS dist_from_50k,
    MOD(emp_id, 3) AS id_mod_3
FROM employees;