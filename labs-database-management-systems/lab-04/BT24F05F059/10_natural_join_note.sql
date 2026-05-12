USE join_lab;
-- NATURAL JOIN silently matches ALL same-named columns — breaks when schema changes.
SELECT p.title, d.dept_name, d.floor_no
FROM projects AS p
JOIN departments AS d ON p.dept_id = d.dept_id;