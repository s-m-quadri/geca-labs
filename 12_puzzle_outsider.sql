USE join_lab;
SELECT s.name, p.title AS project
FROM project_staff AS ps
JOIN staff    AS s ON s.staff_id = ps.staff_id
JOIN projects AS p ON p.proj_id  = ps.proj_id
WHERE s.dept_id != p.dept_id;