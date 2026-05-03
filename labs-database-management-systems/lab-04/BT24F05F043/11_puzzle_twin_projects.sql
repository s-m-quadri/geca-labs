-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).

SELECT 
    s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id

JOIN projects p ON ps.proj_id = p.proj_id

WHERE p.dept_id = 1
  AND p.title IN ('Riddle-UI', 'Riddle-API')
  
GROUP BY s.staff_id, s.name
HAVING COUNT(DISTINCT p.proj_id) = 2;