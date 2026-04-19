-- Task 6: Select with ORDER BY
-- Show students sorted by age (oldest first)

USE school_db;

-- TODO: SELECT all students ORDER BY age DESC
-- Students in 10th grade
SELECT * FROM students WHERE grade = '10th';
 
-- Students older than 15
SELECT * FROM students WHERE age > 15;
 
-- Students age 15 or 16
SELECT * FROM students WHERE age IN (15, 16);
