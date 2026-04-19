-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only

SELECT d.dept_name
FROM departments d
LEFT JOIN projects p 
    ON d.dept_id = p.dept_id
WHERE p.proj_id IS NULL;

--- Alternative using NOT EXISTS:
-- SELECT d.dept_name
-- FROM departments d
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM projects p
--     WHERE p.dept_id = d.dept_id
-- );