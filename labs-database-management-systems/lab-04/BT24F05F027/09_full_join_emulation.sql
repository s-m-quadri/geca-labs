USE join_lab;



SELECT 
    s.name AS staff_name,
    p.title AS project_title,
    ps.hours
FROM projects p
LEFT JOIN project_staff ps 
    ON p.proj_id = ps.proj_id
LEFT JOIN staff s 
    ON ps.staff_id = s.staff_id

UNION

SELECT 
    s.name AS staff_name,
    p.title AS project_title,
    ps.hours
FROM projects p
RIGHT JOIN project_staff ps 
    ON p.proj_id = ps.proj_id
RIGHT JOIN staff s 
    ON ps.staff_id = s.staff_id;