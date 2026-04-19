-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- Find the one person who has hours on both sibling projects
-- with the same name prefix and the same home department.
SELECT s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
WHERE p.title LIKE 'Riddle-%'
GROUP BY s.name, p.dept_id
HAVING COUNT(DISTINCT p.title) = 2;
SELECT s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
WHERE p.title LIKE 'Riddle-%'
GROUP BY s.name, p.dept_id
HAVING COUNT(DISTINCT p.title) = 2;