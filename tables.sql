-- Lab 0: Table Creation
-- Task: Create a students table with proper structure

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30)
);

-- Verify table creation
DESCRIBE students;
