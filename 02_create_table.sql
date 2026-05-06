-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

<<<<<<< HEAD
CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age INT,
  email VARCHAR(150)
);
=======
-- TODO: Write your CREATE TABLE command here
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
>>>>>>> 4380d56c (BT25S05F003)
