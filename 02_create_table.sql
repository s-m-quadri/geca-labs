-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email, grade

-- Switch to school_db
USE school_db;
CREATE TABLE students(
    id INT,
    name VARCHAR(100),
    age INT,
    email VARCHAR(50),
    grade VARCHAR(5)
);
DESCRIBE students;
