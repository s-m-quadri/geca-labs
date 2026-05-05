-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

SELECT DISTINCT s.name
FROM staff s
WHERE EXISTS (
	SELECT 1
	FROM projects p1
	JOIN projects p2
		ON p1.dept_id = p2.dept_id
	 AND p1.proj_id < p2.proj_id
	 AND SUBSTRING_INDEX(p1.title, '-', 1) = SUBSTRING_INDEX(p2.title, '-', 1)
	JOIN project_staff ps1 ON ps1.proj_id = p1.proj_id AND ps1.staff_id = s.staff_id
	JOIN project_staff ps2 ON ps2.proj_id = p2.proj_id AND ps2.staff_id = s.staff_id
);
