-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: A LEFT JOIN bridging staff to projects captures all staff (including those with no projects).
-- A second LEFT JOIN bridging projects back to staff captures all projects (including those with no staff).
-- A UNION automatically combines the results and drops duplicate rows, simulating a FULL OUTER JOIN.

SELECT s.name, p.title
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
LEFT JOIN projects p ON ps.proj_id = p.proj_id
UNION
SELECT s.name, p.title
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id;