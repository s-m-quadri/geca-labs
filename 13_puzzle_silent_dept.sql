-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
SELECT d.dept_name AS department_name
FROM departments AS d
LEFT JOIN projects AS p ON d.dept_id = p.dept_id
WHERE p.project_id IS NULL; -- This condition ensures we only get departments that have no matching projects, i.e., those that never sponsored a project.   
