USE join_lab;
SELECT s.name AS staff_name, d.dept_name
FROM departments AS d
RIGHT JOIN staff AS s ON d.dept_id = s.dept_id;