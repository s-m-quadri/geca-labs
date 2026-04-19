-- Task 8: Three-way join — staff name, department name, project title, hours

USE join_lab;

-- TODO: From project_staff, join staff and projects (and departments if you want dept_name)
-- Columns: staff.name, departments.dept_name, projects.title, project_staff.hours

select project_staff.hours,staff.name,departments.dept_name,projects.title
from project_staff
join staff on staff.staff_id=project_staff.staff_id
join projects on projects.proj_id=project_staff.proj_id
join departments on departments.dept_id=staff.dept_id;

select * from project_staff;
select * from staff;
select * from projects;
select * from departments;