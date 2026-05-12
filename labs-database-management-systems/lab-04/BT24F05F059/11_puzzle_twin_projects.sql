USE join_lab;
SELECT s.name
FROM staff AS s
WHERE s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 101)
  AND s.staff_id IN (SELECT staff_id FROM project_staff WHERE proj_id = 102);