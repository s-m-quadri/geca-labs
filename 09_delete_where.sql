-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;

-- See which rows will be deleted
SELECT * FROM students WHERE age < 15;

-- Delete students younger than 15
DELETE FROM students WHERE age < 15;

-- Check the remaining rows
SELECT * FROM students;

