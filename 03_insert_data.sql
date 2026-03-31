-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;
INSERT INTO students (id, name, age)
VALUES (1, 'Alice', 15);
 
INSERT INTO students (id, name, age)
VALUES (2, 'Bob', 16);
 
INSERT INTO students (id, name, age)
VALUES (3, 'Charlie', 17);
 
SELECT * FROM students;
-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
