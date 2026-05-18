<<<<<<< HEAD
-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

 SELECT s.name, d.dept_name, p.title, ps.hours
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.project_id = p.project_id
JOIN departments d ON s.dept_id = d.dept_id
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
=======
SELECT staff.name, departments.dept_name, projects.title, project_staff.hours
FROM project_staff
INNER JOIN staff ON project_staff.staff_id = staff.staff_id
INNER JOIN projects ON project_staff.proj_id = projects.proj_id
INNER JOIN departments ON staff.dept_id = departments.dept_id
ORDER BY staff.name, projects.title;
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
