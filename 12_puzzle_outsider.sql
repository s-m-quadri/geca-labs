USE join_lab;

SELECT s.name,
       p.title
FROM staff AS s
JOIN project_staff AS ps
  ON s.staff_id = ps.staff_id
JOIN projects AS p
  ON ps.proj_id = p.proj_id
WHERE s.dept_id <> p.dept_id;