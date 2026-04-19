-- Task 8: Update Multiple
-- Change grade for all 10th graders to '10th-A'

USE school_db;
update students set grade = '10th-A' where grade = '10th';
-- TODO: UPDATE students SET grade = '10th-A' WHERE grade = '10th';
