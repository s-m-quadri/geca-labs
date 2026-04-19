-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
select s.name
from staff s
join project_staff ps on s.staff_id=ps.staff_id
join projects p on ps.proj_id=p.proj_id
where p.title like 'Riddle%' 
group by s.name
having count(distinct p.proj_id)>1;