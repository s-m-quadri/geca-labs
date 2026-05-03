-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (id, name, age, email)
VALUES (1, 'Alice', 15, 'alice@school.com');
 
INSERT INTO students (id, name, age, email)
VALUES (2, 'Bob', 16, 'bob@school.com');
 
INSERT INTO students (id, name, age, email)
VALUES (3, 'Charlie', 17, 'charlie@school.com');
 
SELECT * FROM students;