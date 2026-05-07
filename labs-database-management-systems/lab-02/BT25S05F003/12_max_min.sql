-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
