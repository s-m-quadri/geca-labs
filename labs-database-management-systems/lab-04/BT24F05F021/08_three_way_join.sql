-- Task 8: Three-way join — staff name, department name, project title, hours
USE join_lab;

-- Multi-way join to link staff, their departments, and their project assignments
SELECT 
    s.name AS staff_name, 
    d.dept_name, 
    p.title AS project_title, 
    ps.hours
FROM project_staff ps
JOIN staff s ON ps.staff_id = s.staff_id
JOIN projects p ON ps.project_id = p.project_id
JOIN departments d ON s.dept_id = d.dept_id;
