-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students VALUES  (1, 'ALICE', 20,'alice@school.edu');
INSERT INTO students VALUES  (2, 'BOB', 22,'bob@school.edu');
INSERT INTO students VALUES  (3, 'CHARLIE', 19,'charlie@school.edu');
select * from students;