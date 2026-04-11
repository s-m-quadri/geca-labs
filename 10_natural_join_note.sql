-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

SELECT projects.title, departments.dept_name, departments.floor_no
FROM projects
INNER JOIN departments ON projects.dept_id = departments.dept_id;

-- Optional explanation: NATURAL JOIN is risky in real schemas because if unrelated tables happen to have identically named columns added later (like 'created_at', 'id', or 'status'), the database will implicitly try to join on those columns too, leading to unpredictable and incorrect results. Explicit ON clauses are always safer.