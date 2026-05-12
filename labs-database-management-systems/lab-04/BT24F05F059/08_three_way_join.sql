USE join_lab;
SELECT s.name AS staff, d.dept_name, p.title AS project, ps.hours
FROM project_staff AS ps
JOIN staff       AS s ON s.staff_id = ps.staff_id
JOIN projects    AS p ON p.proj_id  = ps.proj_id
JOIN departments AS d ON d.dept_id  = p.dept_id;