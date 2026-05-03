USE join_lab;

-- Strategy:
-- 1) Get all projects (even those with no assignments) using LEFT JOIN
-- 2) UNION with staff who never appear in project_staff (anti-join)

USE join_lab;

-- Strategy:
-- 1) LEFT JOIN → all projects (with or without staff)
-- 2) UNION → add staff who are not assigned to any project

SELECT 
  p.title,
  s.name
FROM projects p
LEFT JOIN project_staff ps 
  ON p.proj_id = ps.proj_id
LEFT JOIN staff s 
  ON ps.staff_id = s.staff_id

UNION

SELECT 
  NULL AS title,
  s.name
FROM staff s
LEFT JOIN project_staff ps 
  ON s.staff_id = ps.staff_id
WHERE ps.proj_id IS NULL;
