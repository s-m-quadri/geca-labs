-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;
ALTER TABLE students
MODIFY COLUMN age TINYINT NOT NULL;
DESCRIBE students;

-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
