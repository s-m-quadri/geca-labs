-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
-- select * from students1;
-- Update students1 set age=19 where student_id=2;
select * from students1;
update students1 set grade='A+' where student_id=2;
select * from students1;