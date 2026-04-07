-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
-- Strategy: Use LEFT JOIN to get all staff and their projects, then UNION with a LEFT JOIN to get all projects and their staff, filtering out the ones that already appear in the first query.
SELECT staff.name AS staff_name, projects.title AS project_title
FROM staff
LEFT JOIN project_staff ON staff.staff_id = project_staff.staff_id
LEFT JOIN projects ON project_staff.proj_id = projects.proj_id
UNION
SELECT staff.name, projects.title
FROM projects
LEFT JOIN project_staff ON projects.proj_id = project_staff.proj_id
LEFT JOIN staff ON project_staff.staff_id = staff.staff_id
WHERE staff.staff_id IS NULL
ORDER BY staff_name, project_title;    