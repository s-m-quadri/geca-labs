-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
USE join_lab;

SELECT 
    staff.name, 
    projects.title
FROM staff
JOIN project_staff 
    ON staff.staff_id = project_staff.staff_id
JOIN projects 
    ON project_staff.project_id = projects.project_id
WHERE staff.dept_id <> projects.dept_id;