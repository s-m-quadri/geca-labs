-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

-- Rewrite the left-join pattern using RIGHT JOIN
-- (departments on the left, staff on the right) so every staff appears once.
SLECT 
staff.name,
departments.dept_name
FROM departments
RIGHT JOIN staff ON departments.dept_id = staff.dept_id;
