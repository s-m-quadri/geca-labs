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
JOIN projects ON project_staff.project_id = projects.project_id
JOIN departments ON projects.dept_id = departments.dept_id
WHERE projects.title LIKE 'Twin%' AND departments.dept_name = 'Engineering'
GROUP BY staff.name
HAVING COUNT(DISTINCT projects.project_id) = 2;
            