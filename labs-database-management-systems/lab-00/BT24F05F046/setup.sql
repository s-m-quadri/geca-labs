CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
SELECT DATABASE();

-- tables.sql solution
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30)
);

DESCRIBE students;