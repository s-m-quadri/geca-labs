-- Task 4: Left outer join — all departments, even if no staff

USE join_lab;

SELECT d.dept_name, s.name
FROM departments d
LEFT JOIN staff s ON s.dept_id = d.dept_id
ORDER BY d.dept_id, s.name;
