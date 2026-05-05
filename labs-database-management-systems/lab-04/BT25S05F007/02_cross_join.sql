-- Task 2: Cartesian product (cross join)
-- List every pair (staff.name, project.title). Count rows mentally: |staff| * |projects|

USE join_lab;

SELECT staff.name, projects.title
FROM staff
CROSS JOIN projects;
