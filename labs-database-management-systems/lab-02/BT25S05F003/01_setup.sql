-- Task 1: Setup Database and Table
-- Create database and students table

-- Create database school_db
CREATE DATABASE IF NOT EXISTS school_db;

-- Switch to school_db
USE school_db;

-- Create students table with:
-- id INT PRIMARY KEY AUTO_INCREMENT
-- name VARCHAR(50)
-- age INT
-- grade VARCHAR(10)
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
