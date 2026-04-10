
-- Create database and students table
Create database IF NOT EXISTS school_db;
-- Switch to school_db
Use school_db;

-- Create students table
Create table students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);