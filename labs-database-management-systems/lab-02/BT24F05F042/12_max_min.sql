-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
-- Add 1 year to all 10th graders
UPDATE students
SET age = age + 1
WHERE grade = '10th';
 
SELECT * FROM students WHERE grade = '10th';