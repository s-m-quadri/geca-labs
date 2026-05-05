USE join_lab;

-- Task 9: Emulating FULL OUTER JOIN using UNION of LEFT and RIGHT JOINs
-- This ensures all projects and all staff are included, even if they have no matching record in project_staff.

SELECT projects.title, staff.name
FROM projects
LEFT JOIN project_staff ON projects.proj_id = project_staff.proj_id
LEFT JOIN staff ON project_staff.staff_id = staff.staff_id

UNION

SELECT projects.title, staff.name
FROM projects
RIGHT JOIN project_staff ON projects.proj_id = project_staff.proj_id
RIGHT JOIN staff ON project_staff.staff_id = staff.staff_id;