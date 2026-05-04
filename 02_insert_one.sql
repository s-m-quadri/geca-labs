-- Task 2: Insert One Student
-- Add your first student to the table

USE school_db;

-- TODO: Insert one student record
-- Example: INSERT INTO students (name, age, grade) VALUES ('Alice', 15, '10th');
INSERT INTO students (name, age, grade) VALUES ('John Doe', 16, '11th');
-- Verify the insertion
SELECT * FROM students;

