-- Task 11: Average Age
-- Calculate average age of all students

USE school_db;

-- TODO: SELECT AVG(age) as average_age FROM students;
UPDATE students
SET age = 17, grade = '12th'
WHERE name = 'Bob';
 
SELECT * FROM students WHERE name = 'Bob';