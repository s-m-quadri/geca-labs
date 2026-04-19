-- Task 13: Group By
-- Count students in each grade

USE school_db;

-- TODO: SELECT grade, COUNT(*) as count FROM students GROUP BY grade;
-- Check before deleting
SELECT * FROM students WHERE id = 5;
 
-- Delete
DELETE FROM students WHERE id = 5;
 
-- Verify deletion
SELECT * FROM students;
SELECT COUNT(*) FROM students;