-- Task 2: Cartesian product (cross join)
-- List every pair (staff.name, project.title). Count rows mentally: |staff| * |projects|

USE join_lab;

-- TODO: SELECT staff.name, projects.title
-- FROM staff
-- CROSS JOIN projects;
    select staff.name, projects.title
    from staff, projects; -- This is the old-school way to do a cross join.


SELECT staff.name, projects.title
FROM staff
JOIN projects ON 1=1; -- This is a common trick to achieve a cross join 

