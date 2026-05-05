USE school_db;

SELECT emp_id, full_name, salary,
  ABS(salary - 50000) AS dist_from_50k,
  MOD(emp_id, 3) AS id_mod_3
FROM employees;