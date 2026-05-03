-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy: emulate FULL OUTER JOIN with
-- (projects LEFT JOIN assignments/staff) UNION (staff with no assignments).
SELECT p.title, s.name, ps.hours
FROM projects p
LEFT JOIN project_staff ps ON ps.proj_id = p.proj_id
LEFT JOIN staff s ON s.staff_id = ps.staff_id
UNION
SELECT p.title, s.name, ps.hours
FROM staff s
LEFT JOIN project_staff ps ON ps.staff_id = s.staff_id
LEFT JOIN projects p ON p.proj_id = ps.proj_id
WHERE ps.proj_id IS NULL
ORDER BY title, name;
