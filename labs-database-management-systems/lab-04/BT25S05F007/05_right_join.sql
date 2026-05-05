-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

SELECT staff.name, departments.dept_name
FROM departments
RIGHT JOIN staff ON staff.dept_id = departments.dept_id
ORDER BY staff.name;
