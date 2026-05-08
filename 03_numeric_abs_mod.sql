USE school_db;
SELECT full_name, ABS(salary - 50000) AS diff_from_50k, MOD(emp_id, 3) AS id_mod3
FROM employees;