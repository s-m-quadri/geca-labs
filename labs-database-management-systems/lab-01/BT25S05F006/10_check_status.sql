-- Task 10: Check Status
-- View current database status

-- Show all databases
-- SHOW DATABASES;

-- Use your database
USE school_db;

-- Show all tables
SHOW TABLES;

-- If students table exists, show its structure
DESCRIBE students1;

-- If students table exists, count rows
 SELECT COUNT(*) as total_students FROM students1;

-- View all data
SELECT * FROM students1;
 SELECT student_name FROM students1;