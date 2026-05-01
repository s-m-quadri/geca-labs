<<<<<<< HEAD
-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: Use UNION of two LEFT JOINs to emulate FULL OUTER JOIN
-- First part: LEFT JOIN staff with project_staff
-- Second part: LEFT JOIN projects with project_staff
 SELECT s.name, p.title
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
LEFT JOIN projects p ON ps.project_id = p.project_id

UNION

 SELECT s.name, p.title
FROM projects p
LEFT JOIN project_staff ps ON p.project_id = ps.project_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id
=======
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
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
