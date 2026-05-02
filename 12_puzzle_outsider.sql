-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

SELECT 
    staff.name,
    projects.title
FROM staff
JOIN departments d_staff 
    ON staff.dept_id = d_staff.dept_id
JOIN project_staff 
    ON staff.staff_id = project_staff.staff_id
JOIN projects 
    ON project_staff.project_id = projects.project_id
JOIN departments d_project 
    ON projects.dept_id = d_project.dept_id
WHERE d_staff.dept_id <> d_project.dept_id;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
