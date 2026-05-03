-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
-- Sort by age (youngest first)
SELECT * FROM students ORDER BY age ASC;
 
-- Sort by age (oldest first)
SELECT * FROM students ORDER BY age DESC;
 
-- Sort by name alphabetically
SELECT * FROM students ORDER BY name ASC;