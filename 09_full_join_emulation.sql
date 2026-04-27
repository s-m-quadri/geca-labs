-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- Strategy:
-- 1) LEFT JOIN: all projects + matching staff
-- 2) RIGHT JOIN: all staff + matching projects
-- 3) UNION removes duplicates → simulates FULL OUTER JOIN

SELECT 
    projects.title,
    staff.name,
    project_staff.hours
FROM projects
LEFT JOIN project_staff 
    ON projects.project_id = project_staff.project_id
LEFT JOIN staff 
    ON project_staff.staff_id = staff.staff_id

UNION

SELECT 
    projects.title,
    staff.name,
    project_staff.hours
FROM projects
RIGHT JOIN project_staff 
    ON projects.project_id = project_staff.project_id
RIGHT JOIN staff 
    ON project_staff.staff_id = staff.staff_id;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
