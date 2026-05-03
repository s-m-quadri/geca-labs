-- Task 9: Drop Table
-- Drop (delete) the students table

USE school_db;

DROP TABLE IF EXISTS students;
-- Warning: This will permanently delete the table!

SHOW TABLES LIKE 'students';
