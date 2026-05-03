SELECT s.name
FROM staff s
JOIN project_staff ps ON ps.staff_id = s.staff_id
JOIN projects p ON p.project_id = ps.project_id
JOIN projects p2 
  ON p.dept_id = p2.dept_id
  AND p.project_id < p2.project_id
  AND SUBSTRING_INDEX(p.title, ' ', 1) = SUBSTRING_INDEX(p2.title, ' ', 1)
JOIN project_staff ps2 
  ON ps2.staff_id = s.staff_id 
  AND ps2.project_id = p2.project_id
GROUP BY s.staff_id, s.name
HAVING COUNT(DISTINCT p.project_id) = 1;