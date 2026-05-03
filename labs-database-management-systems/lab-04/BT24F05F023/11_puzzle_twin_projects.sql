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
JOIN departments ON staff.dept_id = departments.dept_id
WHERE projects.title LIKE 'Twin%' -- Assuming the sibling projects have a common prefix like 'Twin
AND projects.dept_id = staff.dept_id -- Ensure the project is in the same department as the staff
GROUP BY staff.name
HAVING COUNT(DISTINCT projects.proj_id) = 2; -- Ensure the staff
-- booked hours on both sibling projects (2 distinct projects with the same prefix)
