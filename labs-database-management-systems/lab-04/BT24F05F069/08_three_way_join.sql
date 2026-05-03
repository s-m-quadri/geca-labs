-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
SELECT 
    s.name AS staff_name, 
    d.dept_name, 
    p.title AS project_title, 
    ps.hours
FROM staff s
INNER JOIN departments d ON s.dept_id = d.dept_id
INNER JOIN project_staff ps ON s.staff_id = ps.staff_id
INNER JOIN projects p ON ps.project_id = p.project_id;