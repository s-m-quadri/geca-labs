-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

SELECT
  s.name AS staff_name,
  d.dept_name,
  p.title AS project_title,
  ps.hours
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.proj_id = p.proj_id
JOIN departments d ON s.dept_id = d.dept_id;
-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
