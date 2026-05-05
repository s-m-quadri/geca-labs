-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

-- TODO: Rewrite the left-join pattern using RIGHT JOIN
-- (departments on the left, staff on the right) so every staff appears once.

SELECT s.name AS staff_name, d.dept_name AS department_name
FROM departments AS d
RIGHT JOIN staff AS s ON s.dept_id = d.dept_id
ORDER BY s.name;    