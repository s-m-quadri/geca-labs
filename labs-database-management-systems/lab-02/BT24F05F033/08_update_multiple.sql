-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

UPDATE students SET grade = '10th-A' WHERE grade = '10th';
