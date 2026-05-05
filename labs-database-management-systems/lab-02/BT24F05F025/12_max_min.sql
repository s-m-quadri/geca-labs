-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;
select max(age) as oldest, min(age) as youngest from students;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
