-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

--selecting data base
USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);

ALTER TABLE students
MODIFY id INT PRIMARY KEY AUTO_INCREMENT;
 
DESCRIBE students;