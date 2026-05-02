-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
USE join_lab;
SELECT s.name
FROM staff AS s
WHERE s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 101)
  AND s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 102);