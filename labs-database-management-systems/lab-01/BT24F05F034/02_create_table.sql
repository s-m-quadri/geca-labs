-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
    CREATE TABLE IF NOT EXISTS student(
    id INT,
    name VARCHAR(30),
    age INT,
    email VARCHAR(30)
    );