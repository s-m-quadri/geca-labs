-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
FROM project_staff
JOIN staff ON project_staff.staff_id = staff.staff_id
JOIN projects ON project_staff.project_id = projects.project_id
JOIN departments ON staff.dept_id = departments.dept_id
SELECT staff.name, departments.dept_name, projects.title, project_staff.hours
ORDER BY staff.name, projects.title;
