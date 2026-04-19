-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours

SELECT 
    s.name AS staff_name,
    d.dept_name,
    p.title AS project_title,
    ps.hours FROM staff s LEFT JOIN project_staff ps ON s.staff_id = ps.staff_id LEFT JOIN projects p ON ps.proj_id = p.proj_id LEFT JOIN departments d  ON s.dept_id = d.dept_id
ORDER BY s.staff_id, p.proj_id;

-- second
SELECT 
    p.title AS project_title,
    s.name AS staff_name,
    d.dept_name,
    ps.hours
FROM projects p
LEFT JOIN project_staff ps ON p.proj_id = ps.proj_id
LEFT JOIN staff s ON ps.staff_id = s.staff_id
LEFT JOIN departments d ON s.dept_id = d.dept_id
ORDER BY p.proj_id, s.staff_id;