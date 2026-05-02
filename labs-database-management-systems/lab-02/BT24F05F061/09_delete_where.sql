-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;

-- TODO: First, see who will be deleted
-- SELECT * FROM students WHERE age < 15;

-- TODO: Then delete them
-- DELETE FROM students WHERE age < 15;

-- TODO: Check result
-- SELECT * FROM students;
SELECT * FROM students WHERE age < 15;
DELETE FROM students WHERE age < 15;
SELECT * FROM students;

