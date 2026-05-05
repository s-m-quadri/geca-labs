-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

-- TODO: SELECT projects.title, departments.dept_name, departments.floor_no
-- FROM projects
-- INNER JOIN departments ON ...

-- Optional: explain in one line why NATURAL JOIN is risky in real schemas


USE join_lab;

-- Explicitly joining projects and departments on dept_id
SELECT 
    projects.title, 
    departments.dept_name, 
    departments.floor_no
FROM projects
INNER JOIN departments ON projects.dept_id = departments.dept_id;

-- Risk: NATURAL JOIN is dangerous because it breaks if someone adds a column 
-- with a matching name (like 'created_at') to both tables, causing an accidental join.