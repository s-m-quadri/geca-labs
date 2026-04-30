USE school_db;

-- Count students in each grade
SELECT 
    grade,
    COUNT(*) AS count
FROM students
GROUP BY grade;