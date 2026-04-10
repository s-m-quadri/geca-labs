-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;
select dept_name
from departments d
left join projects p on d.dept_id = p.dept_id
where p.proj_id is null;
-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
