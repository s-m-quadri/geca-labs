-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

SELECT projects.title, departments.dept_name, departments.floor_no
FROM projects
INNER JOIN departments ON projects.dept_id = departments.dept_id;

-- NATURAL JOIN is risky because it implicitly joins on all columns with matching names;
-- if schema changes add a common column name (e.g., 'name'), the join semantics change unexpectedly.
