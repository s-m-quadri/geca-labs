-- Task 1: Setup Database and Table
-- Create database and students table
-- Create database
CREATE DATABASE school_db;

-- Use the database
USE school_db;

-- Create students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
-- TODO: Create database school_db

-- TODO: Switch to school_db

-- TODO: Create students table with:
-- id INT PRIMARY KEY AUTO_INCREMENT
-- name VARCHAR(50)
-- age INT
-- grade VARCHAR(10)
