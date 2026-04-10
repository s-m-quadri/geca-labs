-- Task 9: Delete with WHERE
-- Remove students younger than 15

USE school_db;


SELECT * FROM students WHERE age < 15;


DELETE FROM students WHERE age < 15;


SELECT * FROM students;
