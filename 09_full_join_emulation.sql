-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: Use UNION of LEFT JOIN and anti-join pattern to emulate FULL OUTER JOIN
-- This shows all projects with their assigned staff, plus staff with no assignments, plus projects with no staff
SELECT COALESCE(p.title, 'No Project') AS project_title, COALESCE(s.name, 'Unassigned') AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id
UNION
SELECT 'No Project', s.name
FROM staff s
WHERE NOT EXISTS (SELECT 1 FROM project_staff ps WHERE ps.staff_id = s.staff_id)
ORDER BY project_title, staff_name;
