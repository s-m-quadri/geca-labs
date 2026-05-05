-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  age INT,
  email VARCHAR(100)
);

SHOW TABLES;
DESCRIBE students;