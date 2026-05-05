-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
select dept_name
from departments
left join projects on departments.dept_id = projects.dept_id
where projects.project_id is null; -- no matching project       