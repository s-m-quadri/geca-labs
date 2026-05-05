-- Task 3: Inner join — staff with their department name

USE join_lab;

-- TODO: SELECT staff.name, departments.dept_name
-- FROM staff
-- INNER JOIN departments ON staff.dept_id = departments.dept_id;

USE join_lab;
SELECT s.name AS staff_name, p.title AS project_title
FROM staff AS s
CROSS JOIN projects AS p;