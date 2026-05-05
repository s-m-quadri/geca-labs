-- Task 15: Check Status
-- View complete database status

-- Show all databases in the server
SHOW DATABASES;

-- Switch to your database
USE school_db;

-- Show all tables in the current database
SHOW TABLES;

-- Display table structure
DESCRIBE students;

-- Count total rows in the table
SELECT COUNT(*) AS total_students 
FROM students;

-- Display all student records
SELECT * 
FROM students;

-- Summary statistics grouped by grade
SELECT grade, COUNT(*) AS count, AVG(age) AS avg_age
FROM students
GROUP BY grade;