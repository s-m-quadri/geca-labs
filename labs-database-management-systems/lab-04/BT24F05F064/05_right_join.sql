-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

-- TODO: Rewrite the left-join pattern using RIGHT JOIN
-- (departments on the left, staff on the right) so every staff appears once.
USE join_lab;
SELECT s.name AS staff_name, d.dept_name
FROM departments d
RIGHT JOIN staff s ON d.dept_id = s.dept_id;    