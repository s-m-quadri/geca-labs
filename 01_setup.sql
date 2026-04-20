-- Task 1: Setup Database and Table
-- Create database and students table

CREATE DATABASE school_db;

USE school_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);



