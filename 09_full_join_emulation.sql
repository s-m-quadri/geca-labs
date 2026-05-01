-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
-- Part 1: all valid matches (staff ↔ project)
SELECT 
    staff.name,
    departments.dept_name,
    projects.title,
    project_staff.hours
FROM project_staff
JOIN staff 
    ON project_staff.staff_id = staff.staff_id
JOIN projects 
    ON project_staff.proj_id = projects.proj_id   -- FIX HERE
JOIN departments 
    ON staff.dept_id = departments.dept_id;