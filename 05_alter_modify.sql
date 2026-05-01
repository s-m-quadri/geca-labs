-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;

ALTER TABLE students MODIFY COLUMN age TINYINT NOT NULL;

SHOW COLUMNS FROM students LIKE 'age';
