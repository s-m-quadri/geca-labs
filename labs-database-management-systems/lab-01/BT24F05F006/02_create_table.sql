-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100)
);
-- TODO: Write your CREATE TABLE command here
