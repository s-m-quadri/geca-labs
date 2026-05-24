-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

-- TODO: SELECT projects.title, departments.dept_name, departments.floor_no
-- FROM projects
-- INNER JOIN departments ON projects.dept_id = departments.dept_id

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas
-- NATURAL JOIN relies on column names matching, which can lead to unexpected joins if schemas change or have unintended name overlaps.
