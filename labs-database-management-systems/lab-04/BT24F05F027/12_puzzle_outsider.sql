USE join_lab;

SELECT 
    s.name,
    p.title
FROM project_staff ps
JOIN staff s 
    ON ps.staff_id = s.staff_id
JOIN projects p 
    ON ps.proj_id = p.proj_id
WHERE s.dept_id <> p.dept_id;