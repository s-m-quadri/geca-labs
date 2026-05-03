-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
select staff.name
from project_staff
join staff on project_staff.staff_id = staff.staff_id
join projects on project_staff.project_id = projects.project_id
join departments on projects.dept_id = departments.dept_id
where projects.title like 'Twin%' -- same name prefix
group by staff.name
having count(distinct projects.project_id) = 2; -- booked hours on both projects    