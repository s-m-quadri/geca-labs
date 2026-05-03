-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
-- First 3 students
SELECT * FROM students LIMIT 3;
 
-- Top 2 oldest students
SELECT * FROM students ORDER BY age DESC LIMIT 2;