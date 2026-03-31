SELECT p.title AS project_title, s.name AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id  
LEFT JOIN staff s ON ps.staff_id = s.staff_id
UNION
SELECT p.title AS project_title, s.name AS staff_name
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
LEFT JOIN projects p ON ps.proj_id = p.proj_id
WHERE p.proj_id IS NULL;