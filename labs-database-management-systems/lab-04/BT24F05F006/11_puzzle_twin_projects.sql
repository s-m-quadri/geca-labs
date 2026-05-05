-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

SELECT s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.project_id = p.project_id
GROUP BY s.staff_id, s.name, p.dept_id
HAVING 
    COUNT(DISTINCT p.project_id) >= 2
    AND COUNT(DISTINCT LEFT(p.title, 3)) = 1;

-- TODO: Write one SELECT that returns exactly one name (the solver).
