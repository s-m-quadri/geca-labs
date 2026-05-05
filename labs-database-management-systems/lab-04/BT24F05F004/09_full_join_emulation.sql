-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
-- Strategy: combine assigned pairs, unassigned staff, and unassigned projects with UNION ALL.

SELECT staff.name, projects.title, project_staff.hours
FROM project_staff
JOIN staff ON project_staff.staff_id = staff.staff_id
JOIN projects ON project_staff.project_id = projects.project_id 
UNION ALL
SELECT staff.name, NULL AS title, NULL AS hours
FROM staff
LEFT JOIN project_staff ON staff.staff_id = project_staff.staff_id
WHERE project_staff.staff_id IS NULL
UNION ALL
SELECT NULL AS name, projects.title, NULL AS hours
FROM projects
LEFT JOIN project_staff ON projects.project_id = project_staff.project_id
WHERE project_staff.project_id IS NULL
ORDER BY name, title;               

