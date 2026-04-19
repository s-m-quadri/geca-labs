-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
SELECT DISTINCT s.name
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
JOIN departments d ON p.dept_id = d.dept_id
WHERE p.title LIKE 'Twin%' AND d.dept_name = 'Engineering'
GROUP BY s.name
HAVING COUNT(DISTINCT p.proj_id) = 2;

