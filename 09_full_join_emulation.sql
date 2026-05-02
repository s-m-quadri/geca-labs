-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy

-- Strategy: Use UNION of two LEFT JOINs: first from projects to staff via project_staff, second from staff to projects via project_staff with WHERE projects.proj_id IS NULL to get staff not assigned.
SELECT projects.title, staff.name, project_staff.hours
FROM projects
LEFT JOIN project_staff ON projects.proj_id = project_staff.proj_id
LEFT JOIN staff ON project_staff.staff_id = staff.staff_id
UNION
SELECT projects.title, staff.name, project_staff.hours
FROM staff
LEFT JOIN project_staff ON staff.staff_id = project_staff.staff_id
LEFT JOIN projects ON project_staff.proj_id = projects.proj_id
WHERE projects.proj_id IS NULL;
