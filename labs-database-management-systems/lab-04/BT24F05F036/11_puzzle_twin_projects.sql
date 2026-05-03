-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
Select s.name
From staff s
Join project_staff ps ON s.staff_id = ps.staff_id
Join projects p ON ps.proj_id = p.proj_id
Join departments d ON p.dept_id = d.dept_id
Where p.title LIKE 'Riddle-%'
Group By s.name
Having Count(Distinct p.proj_id) = 2;
