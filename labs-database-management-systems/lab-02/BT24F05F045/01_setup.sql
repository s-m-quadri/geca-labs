-- Task 1:
 
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;
USE school_db;


CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
