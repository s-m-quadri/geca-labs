-- Task 3: Insert Multiple Students
-- Add 3 more students in one command

USE school_db;

-- TODO: Insert multiple students at once
-- Example: INSERT INTO students (name, age, grade) VALUES
-- ('Bob', 16, '11th'),
-- ('Charlie', 15, '10th'),
-- ('Diana', 17, '12th');
INSERT INTO students (name, age, grade) VALUES
('Soham', 20, 'SY CSE'),
('Guru', 19, 'SY CSE'),
('Shreya', 20, 'SY FS');
SELECT * FROM students; 