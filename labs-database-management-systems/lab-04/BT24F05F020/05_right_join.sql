-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

SELECT d.dept_name, s.name
FROM departments d
RIGHT JOIN staff s ON s.dept_id = d.dept_id
ORDER BY s.staff_id;
