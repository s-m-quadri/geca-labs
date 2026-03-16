-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
SELECT * FROM students WHERE grade = '10th'; -- Check before update
UPDATE students SET grade = '10th-A' WHERE grade = '10th'; -- Update grade
SELECT * FROM students WHERE grade = '10th-A'; -- Check after update