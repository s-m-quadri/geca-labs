-- Lab 0: Database Setup
-- Task: Create a database named "student_db" and use it

-- TODO: Complete the following

-- Step 1: Create database
-- CREATE DATABASE IF NOT EXISTS ...;

-- Step 2: Use the database
-- USE ...;

-- Step 3: Display current database
-- SELECT DATABASE();
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
SELECT DATABASE();

-- tables.sql solution
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30)
);

DESCRIBE students;