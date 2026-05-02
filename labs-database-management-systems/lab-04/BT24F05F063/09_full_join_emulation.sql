USE join_lab;

-- Part 1: Projects and their staff (including projects with no staff)
SELECT 
    p.title AS project_title, 
    s.name AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id

UNION

-- Part 2: Staff and their projects (including staff with no projects)
SELECT 
    p.title AS project_title, 
    s.name AS staff_name
FROM projects p
RIGHT JOIN project_staff ps ON p.proj_id = ps.proj_id
RIGHT JOIN staff s ON ps.staff_id = s.staff_id;