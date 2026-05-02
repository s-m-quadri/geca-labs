-- Task 10: Count Students
-- Count total number of students

USE school_db;

-- TODO: SELECT COUNT(*) as total_students FROM students;

SELECT * FROM students WHERE grade = '10th';
SELECT * FROM students WHERE age > 15;
SELECT * FROM students WHERE age IN (15, 16);