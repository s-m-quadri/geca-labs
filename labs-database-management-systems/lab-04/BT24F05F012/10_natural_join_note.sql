-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

-- TODO: SELECT projects.title, departments.dept_name, departments.floor_no
-- FROM projects
-- INNER JOIN departments ON ...

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas

SELECT projects.title, departments.dept_name, departments.floor_no
FROM projects
INNER JOIN departments ON projects.dept_id = departments.dept_id;

-- NATURAL JOIN is risky because it joins on all columns with the same name, which can accidentally join on unintended columns if schemas change.
