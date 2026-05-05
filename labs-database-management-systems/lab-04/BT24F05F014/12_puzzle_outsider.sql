-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
USE join_lab;
SELECT s.name, p.title AS project
FROM project_staff AS ps
JOIN staff    AS s ON s.staff_id = ps.staff_id
JOIN projects AS p ON p.proj_id  = ps.proj_id
WHERE s.dept_id != p.dept_id;


