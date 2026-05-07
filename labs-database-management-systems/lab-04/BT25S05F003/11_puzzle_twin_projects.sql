-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- Solution: Find staff who have hours on both Riddle-UI and Riddle-API (twin projects with same prefix and dept_id=1)
SELECT DISTINCT s.name
FROM staff s
WHERE s.staff_id IN (
  SELECT ps1.staff_id FROM project_staff ps1 WHERE ps1.proj_id = 101
)
AND s.staff_id IN (
  SELECT ps2.staff_id FROM project_staff ps2 WHERE ps2.proj_id = 102
);
