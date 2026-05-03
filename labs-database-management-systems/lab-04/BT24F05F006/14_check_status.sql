-- Sanity check for join_lab

SHOW DATABASES;
USE join_lab;
SHOW TABLES;
SELECT COUNT(*) AS staff_rows FROM staff;
SELECT COUNT(*) AS ps_rows FROM project_staff;
SELECT d.dept_name, COUNT(p.proj_id) AS project_count
FROM departments d
LEFT JOIN projects p ON p.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name;