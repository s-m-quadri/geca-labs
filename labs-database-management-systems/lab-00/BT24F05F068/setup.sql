-- Lab 0: Database Setup
-- Task: Create a database named "student_db" and use it

-- TODO: Complete the following

-- Step 1: Create database
-- CREATE DATABASE IF NOT EXISTS student_db;

-- Step 2: Use the database
-- USE student_db;

-- Step 3: Display current database
-- SELECT DATABASE();

-- Step 4: Create a table named "students"
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);

