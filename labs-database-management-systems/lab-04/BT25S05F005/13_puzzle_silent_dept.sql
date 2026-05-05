USE join_lab;

-- Puzzle C: Finding the "Wallflower" department (no projects)
SELECT d.dept_name
FROM departments d
LEFT JOIN projects p ON d.dept_id = p.dept_id
WHERE p.proj_id IS NULL;