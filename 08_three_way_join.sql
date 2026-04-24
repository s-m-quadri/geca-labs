-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

SELECT s.name,
       d.dept_name,
       p.title,
       ps.hours
FROM project_staff ps
JOIN staff s ON s.staff_id = ps.staff_id
JOIN projects p ON p.proj_id = ps.proj_id
JOIN departments d ON d.dept_id = p.dept_id
ORDER BY s.staff_id, p.proj_id;
