-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
USE join_lab;

-- Strategy: Emulate a FULL OUTER JOIN by taking the UNION of a LEFT JOIN 
-- and a RIGHT JOIN. This captures projects with no staff, staff with no 
-- projects, and those with assignments.

SELECT projects.title, staff.name
FROM projects
LEFT JOIN project_staff ON projects.project_id = project_staff.project_id
LEFT JOIN staff ON project_staff.staff_id = staff.staff_id

UNION

SELECT projects.title, staff.name
FROM projects
RIGHT JOIN project_staff ON projects.project_id = project_staff.project_id
RIGHT JOIN staff ON project_staff.staff_id = staff.staff_id;