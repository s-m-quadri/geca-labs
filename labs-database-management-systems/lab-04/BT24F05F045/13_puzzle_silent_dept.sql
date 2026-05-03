-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
SELECT dept_name
FROM departments
LEFT JOIN projects ON departments.dept_id = projects.dept_id
WHERE projects.proj_id IS NULL;
