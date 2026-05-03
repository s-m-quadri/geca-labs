-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
Select s.name, p.title
From staff s
Join project_staff ps ON s.staff_id = ps.staff_id
Join projects p ON ps.proj_id = p.proj_id   
Join departments d ON p.dept_id = d.dept_id
Where s.dept_id <> d.dept_id;  