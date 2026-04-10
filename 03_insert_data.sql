-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (id, name, age, email)
VALUES (1, 'Amruta', 19, 'amruta@gmail.com'),
       (2, 'Dnyaneshwari', 18, 'dnyaneshwari@gmail.com'),
       (3, 'Akshada', 20, 'akshada@gmail.com');
SELECT * FROM students;