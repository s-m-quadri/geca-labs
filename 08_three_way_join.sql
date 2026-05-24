-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
<<<<<<< HEAD
SELECT 
    staff.name,
    departments.dept_name,
    projects.title,
    project_staff.hours
FROM project_staff
JOIN staff 
    ON project_staff.staff_id = staff.staff_id
JOIN projects 
    ON project_staff.proj_id = projects.proj_id
JOIN departments 
    ON staff.dept_id = departments.dept_id;
=======
USE join_lab;
SELECT s.name AS staff, d.dept_name, p.title AS project, ps.hours
FROM project_staff AS ps
JOIN staff       AS s ON s.staff_id = ps.staff_id
JOIN projects    AS p ON p.proj_id  = ps.proj_id
JOIN departments AS d ON d.dept_id  = p.dept_id;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
