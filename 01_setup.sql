-- Task 1: Setup Database and Table
-- Create database and students table

-- TODO: Create database school_db

-- TODO: Switch to school_db

-- TODO: Create students table with:
-- id INT PRIMARY KEY AUTO_INCREMENT
-- name VARCHAR(50)
-- age INT
-- grade VARCHAR(10)
CREATE DATABASE school_db;
USE school_db;
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
