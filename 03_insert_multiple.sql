-- Task 3: Insert Multiple Students
-- Add 3 more students in one command

USE school_db;

-- TODO: Insert multiple students at once
-- Example: INSERT INTO students (name, age, grade) VALUES
-- ('Bob', 16, '11th'),
-- ('Charlie', 15, '10th'),
-- ('Diana', 17, '12th');
INSERT INTO students (id ,name, age, grade) VALUES (2, 'Bob', 16, '11th'),
(3, 'Charlie', 14, '9th'),
(4, 'Diana', 17, '12th');