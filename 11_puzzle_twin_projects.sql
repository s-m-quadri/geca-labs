-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).

SELECT staff.name
FROM project_staff ps1
JOIN projects p1 ON ps1.project_id = p1.project_id
JOIN project_staff ps2 ON ps1.staff_id = ps2.staff_id
JOIN projects p2 ON ps2.project_id = p2.project_id
JOIN departments d1 ON p1.dept_id = d1.dept_id
JOIN departments d2 ON p2.dept_id = d2.dept_id
JOIN staff ON ps1.staff_id = staff.staff_id
WHERE p1.title LIKE 'Alpha%' AND p2.title LIKE 'Alpha%'
AND d1.dept_id = d2.dept_id
AND p1.project_id != p2.project_id;
