-- Task 3: Inner join — staff with their department name

USE join_lab;

SELECT s.name, d.dept_name
FROM staff s
INNER JOIN departments d ON s.dept_id = d.dept_id;
