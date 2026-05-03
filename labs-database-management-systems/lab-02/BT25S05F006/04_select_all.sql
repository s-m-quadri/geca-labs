-- Task 4: Select All Students
-- View all student records

USE school_db1;

-- TODO: Write SELECT query to show all students
SELECT *FROM students;
Select name from students;

update students set marks=94
where id=7;
update students set marks=95
where id=6;
SELECT *FROM students;