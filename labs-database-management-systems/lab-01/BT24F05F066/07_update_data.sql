-- Task 7: Update Records
-- Update the grade for a specific student

USE school_db;

-- TODO: Write your UPDATE command here
-- Remember to use WHERE clause!
update students set grade='A' where id=1;
SELECT * FROM students;