USE school_db;

-- Show grades that have more than 1 student
SELECT 
    grade,
    COUNT(*) AS count
FROM students
GROUP BY grade
HAVING COUNT(*) > 1;