-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;

-- TODO: First, see who will be deleted
-- SELECT * FROM students WHERE age < 15;

-- TODO: Then delete them
-- DELETE FROM students WHERE age < 15;
DELETE FROM students WHERE 
id = 2 OR id = 6 OR id = 7 OR id = 8 OR id = 9 OR id = 10;

-- TODO: Check result
SELECT * FROM students;
