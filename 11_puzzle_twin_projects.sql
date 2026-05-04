-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
write a query that joins project_staff to projects and departments, filtering for projects with the same name prefix and the same department, and then find the person who booked hours on both projects. You can use string functions to extract the name prefix from the project titles.
select staff.name
from project_staff
join staff on project_staff.staff_id = staff.staff_id
join projects on project_staff.project_id = projects.project_id
join departments on projects.dept_id = departments.dept_id
where projects.title like 'Alpha%' -- Assuming the sibling projects have a common prefix like 'Alpha'
group by staff.name 
having count(distinct projects.project_id) > 1; -- Ensure the person booked hours on both sibling projects

    