-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider

SELECT staff.name, projects.title
FROM project_staff
JOIN staff ON project_staff.staff_id = staff.staff_id
JOIN projects ON project_staff.project_id = projects.project_id
JOIN departments ON staff.dept_id = departments.dept_id
WHERE projects.dept_id != staff.dept_id
ORDER BY staff.name, projects.title;
 