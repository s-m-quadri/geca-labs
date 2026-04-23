-- Task 2: Insert One Student
-- Add your first student to the table

USE school_db;

-- TODO: Insert one student record
-- Example: INSERT INTO students (name, age, grade) VALUES ('Alice', 15, '10th');

DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;
USE school_db;
CREATE TABLE students (
    id    INT PRIMARY KEY AUTO_INCREMENT,
    name  VARCHAR(50) NOT NULL,
    age   INT,
    grade VARCHAR(5)
);
SHOW TABLES;