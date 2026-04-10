-- Task 15: Check Status
-- View complete database status

-- Show databases
SHOW DATABASES;

-- Switch to your database
USE school_db;


-- Show tables
SHOW TABLES;

-- Table structure
DESCRIBE students;

-- Total rows
SELECT COUNT(*) as total_students FROM students;

-- View all data
SELECT * FROM students;

-- Summary by grade
SELECT grade, COUNT(*) as count, AVG(age) as avg_age
FROM students
GROUP BY grade;
