-- Task 10: Check Status
-- View current database status


SHOW DATABASES;
USE school_db;
SHOW TABLES;

DESCRIBE students;

-- If students table exists, count rows
SELECT COUNT(*) as total_students FROM students;

-- View all data
SELECT * FROM students;
