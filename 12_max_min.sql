-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;

select MAX(age) as oldest, MIN(age) as youngest from students;
