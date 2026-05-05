SELECT d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM projects p
    WHERE p.dept_id = d.dept_id
);