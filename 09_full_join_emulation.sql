-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)
USE join_lab;

-- Strategy:
-- 1. Get all staff with their project assignments (if any)
-- 2. Get all projects with their assigned staff (if any)
-- 3. UNION both results to simulate FULL OUTER JOIN behavior

SELECT 
    staff.name AS staff_name,
    projects.title AS project_title,
    project_staff.hours
FROM staff
LEFT JOIN project_staff 
    ON staff.staff_id = project_staff.staff_id
LEFT JOIN projects 
    ON project_staff.project_id = projects.project_id

UNION

SELECT 
    staff.name AS staff_name,
    projects.title AS project_title,
    project_staff.hours
FROM projects
LEFT JOIN project_staff 
    ON projects.project_id = project_staff.project_id
LEFT JOIN staff 
    ON project_staff.staff_id = staff.staff_id;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
