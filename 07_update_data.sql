-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
update students set student_grade = 'A' where student_name = 'Alice Johnson';
update students set student_grade = 'B' where student_name = 'Bob Smith';
update students set student_grade = 'A-' where student_name = 'Charlie Brown';