-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

SELECT s.name
FROM staff s
JOIN project_staff ps ON ps.staff_id = s.staff_id
JOIN projects p ON p.proj_id = ps.proj_id
WHERE p.title LIKE 'Riddle-%'
GROUP BY s.name
HAVING COUNT(DISTINCT p.proj_id) = 2;
-- TODO: Write one SELECT that returns exactly one name (the solver).
