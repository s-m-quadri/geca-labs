USE school_db;
SELECT COUNT(*) AS total FROM students;
SELECT COUNT(*) AS total_10th FROM students WHERE grade = '10th';