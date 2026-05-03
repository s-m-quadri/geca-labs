-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
SELECT * FROM students WHERE id = 1; -- Check before update
UPDATE students SET age = 16 WHERE id = 1; -- Update age
SELECT * FROM students WHERE id = 1; -- Check after update