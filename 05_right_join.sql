USE join_lab;

SELECT staff.name, departments.dept_name
FROM departments
RIGHT JOIN staff
ON staff.dept_id = departments.dept_id;