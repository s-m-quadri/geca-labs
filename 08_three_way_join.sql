-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

 SELECT s.name, d.dept_name, p.title, ps.hours
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.project_id = p.project_id
JOIN departments d ON s.dept_id = d.dept_id
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
