-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
SELECT staff.name
FROM staff
JOIN project_staff ON staff.staff_id = project_staff.staff_id
JOIN projects ON project_staff.proj_id = projects.proj_id
WHERE projects.title LIKE 'Riddle%' -- same name prefix
AND projects.dept_id = (SELECT dept_id FROM projects WHERE title LIKE 'Riddle%' GROUP BY dept_id HAVING COUNT(*) > 1) -- same home department
GROUP BY staff.name
HAVING COUNT(DISTINCT projects.proj_id) = 2; -- booked hours on both projects
