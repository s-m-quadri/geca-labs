-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
SELECT 
    s.name AS outsider_name, 
    p.title AS cross_dept_project
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.project_id = p.project_id
WHERE s.dept_id <> p.dept_id;