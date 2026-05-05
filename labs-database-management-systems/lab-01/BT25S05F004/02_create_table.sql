-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
 CREATE TABLE student_info
 (
    rollno int primary key,
     name varchar(50),
    marks int
    );
DESCRIBE student_info;