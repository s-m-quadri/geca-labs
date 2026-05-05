USE join_lab;

-- Task 3: Inner join — staff with their department name
SELECT staff.name, departments.dept_name
FROM staff
INNER JOIN departments ON staff.dept_id = departments.dept_id;