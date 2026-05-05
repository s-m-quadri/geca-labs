-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

SELECT MAX(age) AS oldest,
       MIN(age) AS youngest
FROM students;