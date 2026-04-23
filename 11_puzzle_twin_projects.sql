-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).

USE join_lab;
SELECT a.name AS person_a, b.name AS person_b
FROM staff AS a
JOIN staff AS b
  ON a.dept_id = b.dept_id AND a.staff_id < b.staff_id;