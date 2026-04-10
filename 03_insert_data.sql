-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students (name, age, email) VALUES ('Alic Johnson', 20, 'ab.johnson@example.com');
INSERT INTO students (name, age, email) VALUES ('Boba Smith', 22, 'b.smith@example.com');
INSERT INTO students (name, age, email) VALUES ('Charlie Brwn', 19, 'chalie.brown@example.com');  
SELECT * FROM students; -- This line is just to verify the data insertion, you can remove it if not needed.