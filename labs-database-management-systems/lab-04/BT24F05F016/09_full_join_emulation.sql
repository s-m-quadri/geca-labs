-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: list matched assignments first, then add unassigned projects and
-- staff who never appear in project_staff using anti-join branches.
SELECT s.name AS staff_name, p.title AS project_title, ps.hours
FROM project_staff ps
JOIN staff s ON s.staff_id = ps.staff_id
JOIN projects p ON p.proj_id = ps.proj_id

UNION ALL

SELECT NULL AS staff_name, p.title AS project_title, NULL AS hours
FROM projects p
LEFT JOIN project_staff ps ON ps.proj_id = p.proj_id
WHERE ps.proj_id IS NULL

UNION ALL

SELECT s.name AS staff_name, NULL AS project_title, NULL AS hours
FROM staff s
LEFT JOIN project_staff ps ON ps.staff_id = s.staff_id
WHERE ps.staff_id IS NULL

ORDER BY project_title, staff_name;
