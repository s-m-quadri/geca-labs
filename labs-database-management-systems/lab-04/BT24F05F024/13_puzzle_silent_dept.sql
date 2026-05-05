-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

SELECT d.dept_name
FROM departments d
LEFT JOIN projects p ON p.dept_id = d.dept_id
WHERE p.proj_id IS NULL;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
