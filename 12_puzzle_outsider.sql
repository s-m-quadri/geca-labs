-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

SELECT s.name, p.title
FROM staff s
JOIN project_staff ps ON ps.staff_id = s.staff_id
JOIN projects p ON p.proj_id = ps.proj_id
WHERE s.dept_id <> p.dept_id
ORDER BY s.name, p.title;
