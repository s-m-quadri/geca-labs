USE join_lab;



SELECT 
    p.title AS project_title,
    s.name AS staff_name,
    ps.hours
FROM projects p
LEFT JOIN project_staff ps ON p.project_id = ps.project_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id

UNION

SELECT 
    p.title AS project_title,
    s.name AS staff_name,
    ps.hours
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
LEFT JOIN projects p ON ps.project_id = p.project_id
WHERE p.project_id IS NULL;