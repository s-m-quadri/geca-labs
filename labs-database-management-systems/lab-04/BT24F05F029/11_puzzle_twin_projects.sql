-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

SELECT s.name
FROM staff s
JOIN project_staff ps1 
    ON s.staff_id = ps1.staff_id
JOIN projects p1 
    ON ps1.project_id = p1.project_id

JOIN project_staff ps2 
    ON s.staff_id = ps2.staff_id
JOIN projects p2 
    ON ps2.project_id = p2.project_id

WHERE 
    p1.dept_id = p2.dept_id
    AND p1.title LIKE CONCAT(LEFT(p2.title, 3), '%')
    AND p1.project_id <> p2.project_id
GROUP BY s.staff_id, s.name
HAVING COUNT(DISTINCT p1.project_id, p2.project_id) >= 1;

-- TODO: Write one SELECT that returns exactly one name (the solver).
