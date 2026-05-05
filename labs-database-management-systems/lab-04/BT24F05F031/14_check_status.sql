SELECT d.dept_name, COUNT(p.proj_id) AS project_count
FROM departments d
LEFT JOIN projects p ON p.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name;