USE join_lab;

SELECT 
    projects.title,
    departments.dept_name,
    departments.floor_no
FROM projects
INNER JOIN departments
    ON projects.dept_id = departments.dept_id;