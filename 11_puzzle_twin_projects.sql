USE join_lab;

<<<<<<< HEAD
SELECT s.name
FROM staff s
JOIN project_staff ps1 ON s.staff_id = ps1.staff_id
JOIN projects p1 ON ps1.proj_id = p1.proj_id
JOIN project_staff ps2 ON s.staff_id = ps2.staff_id
JOIN projects p2 ON ps2.proj_id = p2.proj_id
WHERE p1.dept_id = p2.dept_id
  AND LEFT(p1.title, 6) = LEFT(p2.title, 6)
  AND p1.proj_id <> p2.proj_id
GROUP BY s.staff_id
HAVING COUNT(DISTINCT p1.proj_id) >= 2;
=======
SELECT projects.title,
       departments.dept_name,
       departments.floor_no
FROM projects
INNER JOIN departments
  ON projects.dept_id = departments.dept_id;
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
