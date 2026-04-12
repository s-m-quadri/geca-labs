-- Show all databases
SHOW DATABASES;

-- Use your database
USE school_db;

-- Show all tables
SHOW TABLES;

-- If students table exists, show its structure
DESCRIBE students;

-- If students table exists, count rows
SELECT COUNT(*) AS total_students FROM students;

-- View all data
SELECT * FROM students;