-- Task 13: Group By
-- Count students in each grade

USE school_db;

-- TODO: SELECT grade, COUNT(*) as count FROM students GROUP BY grade;

SELECT grade, COUNT(*) as count FROM students GROUP BY grade;

