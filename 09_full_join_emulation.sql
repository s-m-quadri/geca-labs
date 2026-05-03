-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

-- TODO: Write a query your instructor can run; add a short comment on your strategy
USE join_lab;

-- STRATEGY: Combine a LEFT JOIN (all project assignments + projects without staff)
-- with a RIGHT JOIN (all staff without projects) to find all missing links.

-- Part 1: All projects and their assigned staff (including projects with no staff)
SELECT 
    p.title AS project_title, 
    s.name AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.project_id = ps.project_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id

UNION

-- Part 2: All staff who might not be assigned to any project
SELECT 
    p.title AS project_title, 
    s.name AS staff_name
FROM projects p
RIGHT JOIN project_staff ps ON p.project_id = ps.project_id
RIGHT JOIN staff s ON ps.staff_id = s.staff_id;