-- Task 2: Cartesian product (cross join)
-- List every pair (staff.name, project.title). Count rows mentally: |staff| * |projects|

USE join_lab;
select count(*) from staff;
select count(*) from projects;


-- TODO: SELECT staff.name, projects.title
-- FROM staff
-- CROSS JOIN projects;
