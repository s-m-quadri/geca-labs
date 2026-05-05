-- Show all databases
SHOW DATABASES;

-- Switch to database
USE school_db;

-- Show all tables
SHOW TABLES;

-- Show structure of students table
DESCRIBE students;

-- Total number of students
SELECT COUNT(*) AS total_students
FROM students;

-- View all student data
SELECT * FROM students;

-- Summary by grade
SELECT grade, COUNT(*) AS count, AVG(age) AS avg_age
FROM students
GROUP BY grade;