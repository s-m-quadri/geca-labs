-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

SELECT d.dept_name
FROM departments d
LEFT JOIN projects p ON d.dept_id = p.dept_id
WHERE p.proj_id IS NULL;