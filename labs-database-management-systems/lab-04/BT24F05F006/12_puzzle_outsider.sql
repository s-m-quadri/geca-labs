-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

UUSE join_lab;

SELECT 
    s.name,
    p.title
FROM staff s
JOIN project_staff ps 
    ON s.staff_id = ps.staff_id
JOIN projects p 
    ON ps.project_id = p.project_id
WHERE s.dept_id <> p.dept_id;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
