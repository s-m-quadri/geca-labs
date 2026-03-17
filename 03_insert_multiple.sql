-- Task 3: Insert Multiple Students
-- Add 3 more students in one command

USE school_db;

-- Task 3 solution: Insert multiple students in one query
INSERT INTO students (name, age, grade) VALUES
  ('Riya', 14, '9th'),
  ('Aarav', 16, '11th'),
  ('Simran', 15, '10th');
