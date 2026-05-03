-- Task 1: Setup Database and Table
-- Create database and students table

 Create database school_db;
USE school_db;
Create table students(
 id INT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(50),
 age INT,
 grade VARCHAR(10));
