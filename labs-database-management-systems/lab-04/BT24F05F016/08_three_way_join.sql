-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

SELECT staff.name, departments.dept_name, projects.title, project_staff.hours
FROM project_staff
JOIN staff ON staff.staff_id = project_staff.staff_id
JOIN projects ON projects.proj_id = project_staff.proj_id
JOIN departments ON departments.dept_id = projects.dept_id
ORDER BY staff.name, projects.title;
