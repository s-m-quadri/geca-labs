-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy

-- Strategy:
-- 1. First query: keep all projects (LEFT JOIN)
-- 2. Second query: keep all staff (RIGHT JOIN)
-- 3. Combine using UNION to avoid duplicates

SELECT 
    p.title AS project_title,
    s.name AS staff_name,
    ps.hours
FROM projects p
LEFT JOIN project_staff ps 
    ON p.proj_id = ps.proj_id
LEFT JOIN staff s 
    ON ps.staff_id = s.staff_id

UNION

SELECT 
    p.title AS project_title,
    s.name AS staff_name,
    ps.hours
FROM projects p
RIGHT JOIN project_staff ps 
    ON p.proj_id = ps.proj_id
RIGHT JOIN staff s 
    ON ps.staff_id = s.staff_id;