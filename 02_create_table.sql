
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);
DESCRIBE students;
=======
-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;

-- TODO: Write your CREATE TABLE command here
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100) UNIQUE
);
>>>>>>> 34f8c46e (Done)
