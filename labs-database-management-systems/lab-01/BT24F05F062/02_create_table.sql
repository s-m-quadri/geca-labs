-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    rollnum INT
);
DESCRIBE students;
