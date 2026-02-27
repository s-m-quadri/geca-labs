-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (id, name, age, email)
VALUES (1, 'Amruta', 19, 'amruta@school.com');
 
INSERT INTO students (id, name, age, email)
VALUES (2, 'Dnyaneshwari', 18, 'dnyaneshwari@school.com');
 
INSERT INTO students (id, name, age, email)
VALUES (3, 'Namrata', 17, 'namrata@school.com');
 
SELECT * FROM students;
