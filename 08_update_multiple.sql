-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
UPDATE students SET grade = 'O' WHERE grade = '12th';
UPDATE students SET grade = 'A++' WHERE grade = '10th';
UPDATE students SET grade = 'A+' WHERE grade = '9th';