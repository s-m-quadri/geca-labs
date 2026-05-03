-- Task 10: Check Status
-- View current database status

-- Show all databases
SHOW DATABASES;

-- Use your database
USE school_db;

-- Show all tables
SHOW TABLES;

-- If students table exists, show its structure
DESCRIBE student_info;

-- If students table exists, count rows
SELECT COUNT(*) as total_students FROM student_info;

-- View all data
SELECT * FROM student_info;
