-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;

-- TODO: First, see who will be deleted
-- SELECT * FROM students WHERE age < 15;

-- TODO: Then delete them
-- DELETE FROM students WHERE age < 15;

-- TODO: Check result
-- SELECT * FROM students;
-- Delete one student
DELETE FROM students
WHERE id = 5;
 
-- Delete multiple
DELETE FROM students
WHERE age < 15;
 
-- Always check first with SELECT!
SELECT * FROM students WHERE age < 15;
-- Then delete
DELETE FROM students WHERE age < 15;