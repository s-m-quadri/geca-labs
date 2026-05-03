-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
select staff.name, projects.title
from staff
join project_staff on staff.staff_id = project_staff.staff_id
join projects on project_staff.proj_id = projects.proj_id
where staff.dept_id != projects.dept_id;