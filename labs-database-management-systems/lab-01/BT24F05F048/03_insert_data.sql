-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (id, name, age)
VALUES (1, 'Alice', 20),
       (2, 'Bob', 22),
       (3, 'Charlie', 21);

DESCRIBE students;  
