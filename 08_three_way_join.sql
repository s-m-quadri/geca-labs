-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

 From project_staff, join staff and projects (and departments if you want dept_name)
 staff.name, departments.dept_name, projects.title, project_staff.hours
