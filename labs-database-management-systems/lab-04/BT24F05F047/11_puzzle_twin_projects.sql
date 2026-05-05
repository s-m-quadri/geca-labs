-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
SELECT s.name AS staff_name
FROM staff AS s
JOIN project_staff AS ps ON s.staff_id = ps.staff_id
JOIN projects AS p ON ps.project_id = p.project_id
WHERE p.title LIKE 'Twin%' -- Assuming the sibling projects have a name prefix "Twin"
GROUP BY s.name
HAVING COUNT(DISTINCT p.project_id) = 2; -- Only one person booked hours on both projects, so we check for exactly 2 distinct projects with the "Twin" prefix   

