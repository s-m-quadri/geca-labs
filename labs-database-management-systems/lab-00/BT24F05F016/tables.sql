-- Lab 0: Table Creation
-- Task: Create a students table with proper structure
-- Enhanced with additional fields for better database design

USE student_db;

-- TODO: Create students table with the following columns:
-- - id (integer, primary key)
-- - name (string, max 50 characters, not null)
-- - age (integer)
-- - department (string, max 30 characters)

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 18),
    department VARCHAR(30),
    cgpa DECIMAL(3,2),
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verify table creation
DESCRIBE students;
SHOW CREATE TABLE students;
