-- Task 5: Select with WHERE
-- Find students in 10th grade

USE school_db;

-- TODO: SELECT students WHERE grade = '10th'

-- Students in 10th grade
SELECT * FROM students WHERE grade = '10th';
 
-- Students older than 15
SELECT * FROM students WHERE age > 15;
 
-- Students age 15 or 16
SELECT * FROM students WHERE age IN (15, 16);