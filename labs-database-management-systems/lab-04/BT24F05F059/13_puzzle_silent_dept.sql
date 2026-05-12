USE join_lab;
SELECT d.dept_name
FROM departments AS d
LEFT JOIN projects AS p ON p.dept_id = d.dept_id
WHERE p.proj_id IS NULL;