-- Task 3: Inner join — staff with their department name

USE join_lab;

-- TODO: SELECT staff.name, departments.dept_name
-- FROM staff
-- INNER JOIN departments ON staff.dept_id = departments.dept_id;
SELECT s.name, d.dept_name
FROM staff s
INNER JOIN departments d
ON s.dept_id = d.dept_id;                                                                  