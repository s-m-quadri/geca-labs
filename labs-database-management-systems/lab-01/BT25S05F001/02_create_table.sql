-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;
CREATE TABLE students (
    id INT,
    name VARCHAR(40),
    age INT,
    email VARCHAR(50)
);
DESCRIBE students;

-- TODO: Write your CREATE TABLE command here
