-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;
ALTER TABLE students
MODIFY COLUMN mobile_number VARCHAR(12);
 
DESCRIBE students1;
-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
