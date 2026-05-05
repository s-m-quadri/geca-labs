-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours
from project_staff
join staff on project_staff.staff_id = staff.staff_id
join projects on project_staff.project_id = projects.project_id
join departments on staff.dept_id = departments.dept_id
select staff.name, departments.dept_name, projects.title, project_staff.hours
order by staff.name, projects.title;    
    