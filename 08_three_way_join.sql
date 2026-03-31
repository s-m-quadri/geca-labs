SELECT staff.name, departments.dept_name, projects.title, project_staff.hours
FROM project_staff
INNER JOIN staff ON project_staff.staff_id = staff.staff_id
INNER JOIN projects ON project_staff.proj_id = projects.proj_id
INNER JOIN departments ON staff.dept_id = departments.dept_id
ORDER BY staff.name, projects.title;