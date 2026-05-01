-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
<<<<<<< HEAD


UPDATE students
SET age = 16
WHERE id = 1;

SELECT * FROM students WHERE id = 1;
=======
-- Good: Updates specific row
-- Good: Updates specific row
UPDATE students
SET age = 16
WHERE id = 1;
 
-- -- Bad: Updates ALL rows!
-- UPDATE students
-- SET age = 16;
>>>>>>> 0aceaf16d7dd047458df8ed27d83009cc30dc5d2
