-- Task 1: Setup Database and Table
-- Create database and students table

CREATE DATABASE IF NOT EXISTS school_db;

USE school_db;

CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(10)
);
