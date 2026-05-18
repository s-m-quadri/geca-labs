-- Task 10: Natural join vs explicit keys
-- Natural join is rare in production. Write the **same result** as an INNER JOIN
-- between projects and departments using ON with column names explicit.

USE join_lab;

<<<<<<< HEAD
 SELECT projects.title, departments.dept_name, departments.floor_no
FROM projects
INNER JOIN departments ON ...
JOIN departments ON projects.dept_id = departments.dept_id

  explain in one line why NATURAL JOIN is risky in real schemas
=======
SELECT projects.title,
       departments.dept_name,
       departments.floor_no
FROM projects
INNER JOIN departments
  ON projects.dept_id = departments.dept_id;

-- NATURAL JOIN is risky because it joins on all identically named columns, which can break when schema changes.
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
