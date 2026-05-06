-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
USE join_lab;
SELECT s.name AS staff_name, p.title AS project_title, d.dept_name
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.project_id = p.project_id
JOIN departments d ON s.dept_id = d.dept_id
WHERE d.dept_id <> p.dept_id; -- staff's dept_id is different from