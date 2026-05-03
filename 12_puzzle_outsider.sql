-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
select staff.name, projects.title
from project_staff
join staff on project_staff.staff_id = staff.staff_id
join projects on project_staff.project_id = projects.project_id
join departments on projects.dept_id = departments.dept_id
where staff.dept_id != departments.dept_id; -- official dept differs from project dept  