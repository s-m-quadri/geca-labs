-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

-- TODO: SELECT projects.title, departments.dept_name, departments.floor_no
-- FROM projects
-- INNER JOIN departments ON ...

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas

SELECT p.title AS project_title, d.dept_name AS department_name, d.floor_no
FROM projects AS p
INNER JOIN departments AS d ON p.dept_id = d.dept_id;   

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas
-- NATURAL JOIN can lead to unexpected results if the schema changes (e.g., new columns are added) or if there are columns with the same name that shouldn't be joined on.

