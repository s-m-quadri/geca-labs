-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

SELECT p.title, d.dept_name, d.floor_no
FROM projects p
INNER JOIN departments d ON p.dept_id = d.dept_id;

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas
-- NATURAL JOIN can silently change behavior if new same-named columns are added.
