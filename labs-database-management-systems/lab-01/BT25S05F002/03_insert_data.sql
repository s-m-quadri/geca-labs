-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (id,name,age,email) VALUES(1,'vedika',20,'vedika@gmail.com');
INSERT INTO students (id,name,age,email) VALUES(2,'vanshita',23,'vanshita@gmail.com');
INSERT INTO students (id,name,age,email) VALUES(3,'prajkta',20,'prajuu@gmail.com');

-- to display data
SELECT * FROM students;