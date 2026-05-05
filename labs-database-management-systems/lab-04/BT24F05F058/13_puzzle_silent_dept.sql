-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only

SELECT a.name AS earlier, b.name AS later
FROM staff AS a
JOIN staff AS b
  ON a.dept_id = b.dept_id AND a.joined_on < b.joined_on;