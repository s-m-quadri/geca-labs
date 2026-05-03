-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
SELECT staff.name, projects.title
FROM staff
JOIN project_staff ON staff.staff_id = project_staff.staff_id
JOIN projects ON project_staff.proj_id = projects.proj_id
JOIN departments ON projects.dept_id = departments.dept_id
WHERE staff.dept_id != departments.dept_id
ORDER BY staff.name, projects.title;    

