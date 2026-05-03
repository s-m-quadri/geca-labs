-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
SELECT s.name AS staff_name, p.title AS project_title
FROM staff AS s
LEFT JOIN project_staff AS ps ON s.staff_id = ps.staff_id
LEFT JOIN projects AS p ON ps.project_id = p.project_id
UNION
SELECT s.name AS staff_name, p.title AS project_title
FROM staff AS s
RIGHT JOIN project_staff AS ps ON s.staff_id = ps.staff_id
RIGHT JOIN projects AS p ON ps.project_id = p.project_id
ORDER BY staff_name, project_title;