-- Task 3: Insert Multiple Students
-- Add 3 more students in one command

USE school_db;

-- TODO: Insert multiple students at once
-- Example: INSERT INTO students (name, age, grade) VALUES
-- ('Bob', 16, '11th'),
-- ('Charlie', 15, '10th'),
-- ('Diana', 17, '12th');
INSERT INTO students (name, age, grade) VALUES
('Jane Smith', 15, '10th'),
('Emily Davis', 17, '12th'),
('Michael Brown', 16, '11th');
-- Verify the insertions
SELECT * FROM students;

