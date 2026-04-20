USE join_lab;

SELECT 
    s.name AS staff_name, 
    d.dept_name, 
    p.title AS project_title, 
    ps.hours
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
JOIN departments d ON s.dept_id = d.dept_id
ORDER BY s.name, p.title;