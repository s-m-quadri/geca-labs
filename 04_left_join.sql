USE join_lab;
SELECT d.dept_name, s.name AS staff_name
FROM departments AS d
LEFT JOIN staff AS s ON d.dept_id = s.dept_id;