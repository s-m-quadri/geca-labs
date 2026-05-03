-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: UNION of (1) all projects with their staff assignments, and (2) staff with no project assignments
-- This captures: matched pairs, orphan projects (no staff), and orphan staff (no projects)

SELECT projects.title, staff.name
FROM projects
LEFT JOIN project_staff ON projects.proj_id = project_staff.proj_id
LEFT JOIN staff ON project_staff.staff_id = staff.staff_id
UNION
SELECT NULL, staff.name
FROM staff
LEFT JOIN project_staff ON staff.staff_id = project_staff.staff_id
WHERE project_staff.staff_id IS NULL;
