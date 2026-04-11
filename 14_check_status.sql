-- Sanity check for join_lab

USE join_lab;

SELECT s.name
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
WHERE p.title LIKE 'Riddle-%'
GROUP BY s.staff_id, s.name
HAVING COUNT(DISTINCT p.proj_id) = 2;