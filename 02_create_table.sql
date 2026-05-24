-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
<<<<<<< HEAD
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);
DESCRIBE students;
=======

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(100)
);
>>>>>>> de8a6c3a (done)
