-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
-- Good: Updates specific row
-- Good: Updates specific row
UPDATE students
SET age = 16
WHERE id = 1;
 
-- -- Bad: Updates ALL rows!
-- UPDATE students
-- SET age = 16;