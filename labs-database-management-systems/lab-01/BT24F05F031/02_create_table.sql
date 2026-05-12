-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command
CREATE TABLE STUDENT
USE school_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(100) UNIQUE
);
=======
-- TODO: Write your CREATE TABLE command here
CREATE TABLE students(
    id int PRIMARY KEY,
    name VARCHAR(50),
    age int NOT NULL,
    email NVARCHAR
);
 (BT24F05F031)
