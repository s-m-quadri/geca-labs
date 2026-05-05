USE join_lab;

SELECT 
    s.name,
    p.title
FROM staff s
JOIN project_staff ps 
    ON s.staff_id = ps.staff_id
JOIN projects p 
    ON ps.proj_id = p.proj_id
WHERE s.dept_id <> p.dept_id;