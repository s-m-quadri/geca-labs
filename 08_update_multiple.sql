-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
USE school_db;
UPDATE students SET age = 17, grade = '12th' WHERE name = 'Bob';
SELECT * FROM students WHERE name = 'Bob';