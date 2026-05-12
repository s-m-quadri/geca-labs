USE school_db;
SELECT grade, COUNT(*) AS count FROM students GROUP BY grade;