USE join_lab;

-- Task 8: Three-way join connecting staff, departments, projects, and hours
SELECT 
    staff.name, 
    departments.dept_name, 
    projects.title, 
    project_staff.hours
FROM project_staff
JOIN staff ON project_staff.staff_id = staff.staff_id
JOIN projects ON project_staff.proj_id = projects.proj_id
JOIN departments ON staff.dept_id = departments.dept_id;