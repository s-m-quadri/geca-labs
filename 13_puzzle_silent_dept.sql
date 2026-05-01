-- Puzzle C (riddle)
-- "One department never sponsored a project. Which `dept_name` is the wallflower?"

USE join_lab;

-- TODO: Use an outer join or NOT EXISTS pattern; return dept_name only
<<<<<<< HEAD
SELECT d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM projects p
    WHERE p.dept_id = d.dept_id
);
=======
USE join_lab;
SELECT d.dept_name
FROM departments AS d
LEFT JOIN projects AS p ON p.dept_id = d.dept_id
WHERE p.proj_id IS NULL;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
