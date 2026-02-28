-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

--selecting database
USE school_db;

-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
INSERT INTO students ( name, age, email) VALUES
 ( 'Mayur', 20, 'Mayur@school.com'),
 ( 'Suraj', 18, 'Suraj@gmail.com'),
 ( 'Anushka', 19, 'Anu@school.com');
 
SELECT * FROM students;