-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

SELECT staff.name, departments.dept_name, projects.title, project_staff.hours
FROM project_staff
JOIN staff ON project_staff.staff_id = staff.staff_id
JOIN projects ON project_staff.proj_id = projects.proj_id
JOIN departments ON staff.dept_id = departments.dept_id;
