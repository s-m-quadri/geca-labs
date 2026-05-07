-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
USE join_lab;
SELECT s.name AS staff_name, p.title AS project_title, d.dept_name
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.project_id = p.project_id
JOIN departments d ON s.dept_id = d.dept_id
WHERE p.title LIKE 'Twin%' -- projects with same name prefix
GROUP BY s.name
HAVING COUNT(DISTINCT p.project_id) = 2; -- only one person booked hours on both