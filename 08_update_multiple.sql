-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';

-- Fix column size (to avoid "Data too long" error)
ALTER TABLE students MODIFY grade VARCHAR(10);

-- Insert sample data
INSERT INTO students (name, age, grade) VALUES
('Bob', 16, '11th'),
('Charlie', 15, '10th'),
('Diana', 17, '12th'),
('Eve', 16, '10th');

-- Update all 10th graders to '10th-A'
UPDATE students 
SET grade = '10th-A' 
WHERE grade = '10th';

-- Display updated table
SELECT * FROM students;
