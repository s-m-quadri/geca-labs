-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
USE join_lab;

SELECT 
    staff.name,
    projects.title
FROM project_staff
JOIN staff 
    ON project_staff.staff_id = staff.staff_id
JOIN projects 
    ON project_staff.proj_id = projects.proj_id
WHERE staff.dept_id <> projects.dept_id;
