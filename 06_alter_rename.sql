-- Task 6: Rename Column
-- Rename 'name' column to 'student_name'

USE school_db;

-- TODO: Write your ALTER TABLE RENAME COLUMN command here
-- MySQL syntax: ALTER TABLE table_name RENAME COLUMN old_name TO new_name;


ALTER TABLE students RENAME COLUMN name TO student_name;




DESCRIBE students;






