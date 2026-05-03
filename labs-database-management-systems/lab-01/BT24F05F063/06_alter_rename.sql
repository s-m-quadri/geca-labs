-- Task 6: Rename Column
-- Rename 'name' column to 'student_name'

USE school_db;

-- TODO: Write your ALTER TABLE RENAME COLUMN command here
-- MySQL syntax: ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
ALTER TABLE students
MODIFY COLUMN phone VARCHAR(20);
 
DESCRIBE students;