-- Puzzle B (riddle)
-- "Someone officially sits in one department but still helps a project owned
--  by another department. Name that person and the **project title** they help with."

USE join_lab;

-- Solution: Find staff whose department differs from project's department (outsider working on project from another dept)
SELECT DISTINCT s.name, p.title
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
WHERE s.dept_id != p.dept_id
ORDER BY s.name, p.title;
