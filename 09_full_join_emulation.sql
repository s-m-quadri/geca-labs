-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Emulate a full outer join by taking all project assignments plus
-- projects with no staff and staff with no projects.
SELECT p.title AS project_title, s.name AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id
UNION
SELECT NULL AS project_title, s.name AS staff_name
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
WHERE ps.proj_id IS NULL;
