-- Task 5: Right outer join (MySQL supports RIGHT JOIN)
-- All staff rows, with department name when present

USE join_lab;

-- TODO: Rewrite the left-join pattern using RIGHT JOIN
-- (departments on the left, staff on the right) so every staff appears once.
select departments.dept_name,staff.name from departments right join staff on staff.dept_id = departments.dept_id order by departments.dept_id,staff.name;