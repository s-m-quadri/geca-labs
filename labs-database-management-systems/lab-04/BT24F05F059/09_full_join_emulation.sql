USE join_lab;
SELECT s.name, d.dept_name
FROM staff AS s LEFT JOIN departments AS d ON s.dept_id = d.dept_id
UNION
SELECT s.name, d.dept_name
FROM staff AS s RIGHT JOIN departments AS d ON s.dept_id = d.dept_id
WHERE s.staff_id IS NULL;