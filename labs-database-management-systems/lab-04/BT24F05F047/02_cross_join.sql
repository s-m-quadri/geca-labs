-- Task 2: Cartesian product (cross join)
-- List every pair (staff.name, project.title). Count rows mentally: |staff| * |projects|

USE join_lab;

-- TODO: SELECT staff.name, projects.title
-- FROM staff
-- CROSS JOIN projects;

SELECT s.name AS staff_name, p.title AS project_title
FROM staff AS s
CROSS JOIN projects AS p;
