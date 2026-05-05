-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
SELECT MAX(age) as oldest, MIN(age) as youngest FROM students WHERE grade = '10th-A';
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students WHERE grade = '10th-A');
