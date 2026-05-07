-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

SELECT departments.dept_name, staff.name
FROM staff
RIGHT JOIN departments ON staff.dept_id = departments.dept_id
ORDER BY departments.dept_id, staff.name;
