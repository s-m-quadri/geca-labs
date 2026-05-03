-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
To emulate a full outer join in MySQL for this task, consider using UNION to combine results from two LEFT JOINs: one starting from projects to get all projects (including those with no staff assignments), and another starting from staff to get staff with no project assignments. Sketch the join shapes: projects --(left)-- project_staff --(left)-- staff for the first part, and staff --(left)-- project_staff --(left)-- projects (with a WHERE to filter unmatched staff) for the second. What keys link projects to project_staff, and project_staff to staff? Also, think about how to include only rows where hours indicate an assignment.
-- Use UNION of two LEFT JOIN paths to emulate FULL OUTER JOIN:
-- projects -> project_staff -> staff for all projects, and
-- staff -> project_staff -> projects to capture staff with no assignments.
SELECT
    p.title AS project_title,
    s.name AS staff_name
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id
UNION
SELECT
    p.title AS project_title,
    s.name AS staff_name
FROM staff s
LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id
LEFT JOIN projects p ON ps.proj_id = p.proj_id
WHERE ps.staff_id IS NULL;