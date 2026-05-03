-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

-- TODO: SELECT projects.title, departments.dept_name, departments.floor_no
-- FROM projects
-- INNER JOIN departments ON ...
SELECT 
    projects.title, 
    departments.dept_name, 
    departments.floor_no
FROM projects
INNER JOIN departments 
    ON projects.dept_id = departments.dept_id;


-- Optional: explain in one line why NATURAL JOIN is risky in real schemas

-- Why NATURAL JOIN is risky:
-- It automatically joins on ALL columns with matching names; if a new column like 'created_at' 
-- is added to both tables later, the query will break or return zero results.