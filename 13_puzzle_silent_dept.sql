-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
NOT EXISTS (SELECT 1 FROM projects WHERE projects.dept_id = departments.dept_id)
ORDER BY departments.dept_id;
SELECT departments.dept_name
FROM departments
WHERE NOT EXISTS (SELECT 1 FROM projects WHERE projects.dept_id = departments.dept_id)
ORDER BY departments.dept_id;   
