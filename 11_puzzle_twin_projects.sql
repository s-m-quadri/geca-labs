USE join_lab;

SELECT s.name
FROM staff s
JOIN project_staff ps1 ON s.staff_id = ps1.staff_id
JOIN project_staff ps2 ON s.staff_id = ps2.staff_id
JOIN projects p1 ON ps1.proj_id = p1.proj_id
JOIN projects p2 ON ps2.proj_id = p2.proj_id
WHERE p1.proj_id <> p2.proj_id
AND p1.dept_id = p2.dept_id
GROUP BY s.name
HAVING COUNT(DISTINCT p1.proj_id) > 1;