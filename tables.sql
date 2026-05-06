-- Lab 0: Table Creation
-- Task: Create a students table with proper structure

USE student_db;

<<<<<<< HEAD
-- TODO: Create students table with the following columns:
-- - id (integer, primary key)
-- - name (string, max 50 characters, not null)
-- - age (integer)
-- - department (string, max 30 characters)

CREATE TABLE students (
    id int primary key,
    name VARCHAR(50),
    age int,
    department varchar(50)
=======
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30)
>>>>>>> 5ca9861c (BT25S05F002)
);

-- Verify table creation
DESCRIBE students;
