-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
<<<<<<< HEAD
SELECT s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id   -- ⚠️ adjust after DESCRIBE
JOIN departments d ON p.dept_id = d.dept_id
WHERE p.title LIKE CONCAT(SUBSTRING_INDEX(p.title, ' ', 1), '%')
GROUP BY s.staff_id
HAVING COUNT(DISTINCT p.title) = 2;
=======
USE join_lab;
SELECT s.name
FROM staff AS s
WHERE s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 101)
  AND s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 102);
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
