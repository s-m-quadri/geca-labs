-- Task 12: MAX and MIN
-- Find oldest and youngest student

USE school_db1;

-- TODO: SELECT MAX(age) as oldest, MIN(age) as youngest FROM students;
select max(marks) as max_marks,min(marks) as min_marks from students;