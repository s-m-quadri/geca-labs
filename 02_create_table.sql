-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
CREATE table student(
    id INT PRIMARY KEY ;
    name VARCHAR(100) NOT NULL ;
    age INT NOT NULL ;
    email VARCHAR(20) NOT NULL ;
);