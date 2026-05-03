-- Task 1: Setup Database and Table
-- Create database and students table

-- Create database
CREATE DATABASE school_db;

-- Switch to the database
USE school_db;

-- Create students table
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);




