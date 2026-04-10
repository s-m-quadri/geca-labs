-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;

-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
INSERT INTO students (id, name, age, email)
VALUES (1, 'Alice', 15, 'alice@school.com');
 
INSERT INTO students (id, name, age, email)
VALUES (2, 'Bob', 16, 'bob@school.com');
 
SELECT * FROM students;