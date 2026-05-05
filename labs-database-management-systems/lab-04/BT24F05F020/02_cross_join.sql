-- Task 2: Cartesian product (cross join)
-- List every pair (staff.name, project.title). Count rows mentally: |staff| * |projects|

USE join_lab;

SELECT s.name, p.title
FROM staff s
CROSS JOIN projects p;
