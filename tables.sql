-- Lab 0: Table Creation
-- Task: Create a students table with proper structure

USE student_db;

-- TODO: Create students table with the following columns:
-- - id (integer, primary key)
-- - name (string, max 50 characters, not null)
-- - age (integer)
-- - department (string, max 30 characters)

-- CREATE TABLE students (
--     ...
-- );

-- Verify table creation
-- DESCRIBE students;

--ans:
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30)
);