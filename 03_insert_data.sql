-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (name, age, email) VALUES ('Adarsh Singh', 22, 'adarsh.singh@example.com');
INSERT INTO students (name, age, email) VALUES ('Krutarth Fulare', 23, 'krutarth.fulare@example.com');
INSERT INTO students (name, age, email) VALUES ('Charlie Puth', 26, 'charlie.puth@example.com'); 
SELECT * FROM students; 