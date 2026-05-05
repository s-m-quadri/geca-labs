-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours

SELECT s.name AS staff_name, d.dept_name AS department_name, p.title AS project_title, ps.hours
FROM project_staff AS ps
JOIN staff AS s ON ps.staff_id = s.staff_id
JOIN projects AS p ON ps.project_id = p.project_id
JOIN departments AS d ON s.dept_id = d.dept_id
ORDER BY s.name, p.title;