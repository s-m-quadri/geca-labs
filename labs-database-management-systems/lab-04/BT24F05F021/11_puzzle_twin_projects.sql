-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
USE join_lab;

-- Identify the person assigned to both 'sibling' projects in the same department
SELECT s.name
FROM staff s
JOIN project_staff ps1 ON s.staff_id = ps1.staff_id
JOIN project_staff ps2 ON s.staff_id = ps2.staff_id
JOIN projects p1 ON ps1.project_id = p1.project_id
JOIN projects p2 ON ps2.project_id = p2.project_id
WHERE p1.project_id < p2.project_id           -- Ensures we are looking at two different projects
  AND p1.dept_id = p2.dept_id                 -- Same 'home' department
  AND SUBSTRING_INDEX(p1.title, ' ', 1) = SUBSTRING_INDEX(p2.title, ' ', 1); -- Shared prefix
  