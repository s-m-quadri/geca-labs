-- Task 11: Average Age
-- Calculate average age of all students

USE school_db;

-- TODO: SELECT AVG(age) as average_age FROM students;
USE school_db;
SELECT AVG(age) AS avg_age FROM students;
SELECT grade, AVG(age) AS avg_age FROM students GROUP BY grade;