-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;

-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
<<<<<<< HEAD
UPDATE students
SET grade = '10th-A'
WHERE grade = '10th';
=======

-- Good: Updates specific row
UPDATE students
SET age = 16
WHERE id = 1;
 
-- Bad: Updates ALL rows!
UPDATE students
SET age = 16;

>>>>>>> 0aceaf16d7dd047458df8ed27d83009cc30dc5d2
