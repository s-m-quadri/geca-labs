-- Task 3: Insert Sample Data
-- Insert 3 student records into the students tabl
USE school_db;
INSERT INTO students (name, age, email) VALUES
    ('Alice', 20, 'alice@example.com'),
    ('Bob',   21, 'bob@example.com'),
    ('Carol', 22, 'carol@example.com');
SELECT * FROM students;
-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
