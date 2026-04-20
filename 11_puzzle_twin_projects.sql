-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).

SELECT DISTINCT s.name
FROM staff s
JOIN project_staff ps1 ON s.staff_id = ps1.staff_id
JOIN project_staff ps2 ON s.staff_id = ps2.staff_id
JOIN projects p1