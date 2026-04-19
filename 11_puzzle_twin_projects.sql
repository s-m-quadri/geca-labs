-- Puzzle A (riddle)
-- "Two sibling projects share a name prefix and the same home department.
--  Only one person booked hours on **both**. Who is it?"
-- Hint: inspect projects.title and project_staff; avoid hard-coding IDs in your
-- final query if you can use titles or dept instead.

USE join_lab;

-- TODO: Write one SELECT that returns exactly one name (the solver).
USE join_lab;

SELECT DISTINCT s.name
FROM projects p1
JOIN projects p2 
    ON p1.dept_id = p2.dept_id
    AND p1.proj_id < p2.proj_id
    AND p1.title LIKE CONCAT(SUBSTRING(p2.title, 1, 3), '%')

JOIN project_staff ps1 
    ON p1.proj_id = ps1.proj_id
JOIN project_staff ps2 
    ON p2.proj_id = ps2.proj_id
    AND ps1.staff_id = ps2.staff_id

JOIN staff s 
    ON s.staff_id = ps1.staff_id;