-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
USE join_lab;

-- Strategy: Combine LEFT JOIN and RIGHT JOIN using UNION 
-- to simulate FULL OUTER JOIN (include unmatched rows from both sides)

-- Part 1: All projects (even if no staff)
SELECT 
    projects.title,
    staff.name,
    project_staff.hours
FROM projects
LEFT JOIN project_staff 
    ON projects.proj_id = project_staff.proj_id
LEFT JOIN staff 
    ON project_staff.staff_id = staff.staff_id

UNION

-- Part 2: All staff (even if not assigned to any project)
SELECT 
    projects.title,
    staff.name,
    project_staff.hours
FROM staff
LEFT JOIN project_staff 
    ON staff.staff_id = project_staff.staff_id
LEFT JOIN projects 
    ON project_staff.proj_id = projects.proj_id;