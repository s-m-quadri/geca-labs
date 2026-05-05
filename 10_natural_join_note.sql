USE join_lab;

-- Task 10: Explicit INNER JOIN instead of NATURAL JOIN
SELECT projects.title, departments.dept_name, departments.floor_no
FROM projects
INNER JOIN departments ON projects.dept_id = departments.dept_id;