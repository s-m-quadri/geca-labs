USE join_lab;

SELECT staff.name, departments.dept_name
FROM staff
INNER JOIN departments
ON staff.dept_id = departments.dept_id;