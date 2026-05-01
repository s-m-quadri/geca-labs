<<<<<<< HEAD

USE join_lab;

SELECT s.name, p.title
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
=======
USE join_lab;

SELECT s.name,
       p.title
FROM staff AS s
JOIN project_staff AS ps
  ON s.staff_id = ps.staff_id
JOIN projects AS p
  ON ps.proj_id = p.proj_id
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
WHERE s.dept_id <> p.dept_id;