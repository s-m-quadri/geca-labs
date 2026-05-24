- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
-- Hint: Restate the riddle in relational terms. Which entity (departments) has a condition (no matching projects)? 
-- Consider an outer join: sketch it in words - departments LEFT JOIN projects on dept_id, then filter for missing on the right (projects side).
-- Alternatively, NOT EXISTS: departments where no project exists with matching dept_id.
-- What keys link the tables? Draw the tables and mark FKs.
