-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;
CREATE TABLE students (
    id INT,
    name VARCHAR(40),
    age TINYINT NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15)
);
DESCRIBE students;
-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
