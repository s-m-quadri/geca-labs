-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy

SELECT 
  p.title,
  s.name,
  ps.hours
FROM projects p
LEFT JOIN project_staff ps 
  ON p.proj_id = ps.proj_id
LEFT JOIN staff s 
  ON ps.staff_id = s.staff_id

UNION

SELECT 
  p.title,
  s.name,
  ps.hours
FROM projects p
RIGHT JOIN project_staff ps 
  ON p.proj_id = ps.proj_id
RIGHT JOIN staff s 
  ON ps.staff_id = s.staff_id;