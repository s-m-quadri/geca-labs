-- Task 10: Count Students
-- Count total number of students

USE school_db;

-- TODO: SELECT COUNT(*) as total_students FROM students;
USE school_db;
SELECT COUNT(*) AS total FROM students;
SELECT COUNT(*) AS total_10th FROM students WHERE grade = '10th';