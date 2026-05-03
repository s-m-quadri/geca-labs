-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;

SELECT * FROM students ORDER BY age ASC;
SELECT * FROM students ORDER BY age DESC;
SELECT * FROM students ORDER BY name ASC;