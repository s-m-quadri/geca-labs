USE join_lab;

SELECT 
    s.staff_id,
    s.name,
    s.dept_id,
    d.dept_name
FROM departments d
RIGHT JOIN staff s
ON d.dept_id = s.dept_id;