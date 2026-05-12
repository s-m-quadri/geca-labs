USE join_lab;
SELECT s.name, d.dept_name
FROM staff AS s
INNER JOIN departments AS d ON s.dept_id = d.dept_id;