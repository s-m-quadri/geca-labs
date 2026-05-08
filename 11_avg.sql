USE school_db;
SELECT AVG(age) AS avg_age FROM students;
SELECT grade, AVG(age) AS avg_age FROM students GROUP BY grade;