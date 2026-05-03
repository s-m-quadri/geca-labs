USE school_db;

-- Find oldest and youngest student
SELECT 
    MAX(age) AS oldest,
    MIN(age) AS youngest
FROM students;