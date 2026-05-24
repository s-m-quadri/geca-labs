-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

-- TODO: Rewrite the left-join pattern using RIGHT JOIN
-- (departments on the left, staff on the right) so every staff appears once.
<<<<<<< HEAD
SELECT departments.dept_name, staff.name
FROM departments
RIGHT JOIN staff
ON staff.dept_id = departments.dept_id;
=======
USE join_lab;
SELECT s.name AS staff_name, d.dept_name
FROM departments AS d
RIGHT JOIN staff AS s ON d.dept_id = s.dept_id;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
