-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

-- TODO: USE school_db;

-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

-- TODO: SELECT * FROM employees;
-- Drop and recreate database
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;

-- Use database
USE school_db;

-- Create employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
);

-- Insert sample data (5+ rows, different departments)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Alice Johnson', 'HR', 35000.00, '2022-01-15', ' 9876543210 '),
('Bob Smith', 'IT', 55000.00, '2021-06-10', '9123456780'),
('Charlie Brown', 'Finance', 50000.00, '2020-03-20', ' 9988776655'),
('Diana Prince', 'IT', 62000.00, '2023-07-05', '9012345678 '),
('Ethan Hunt', 'HR', 40000.00, '2019-11-25', ' 9090909090');

-- View all data
SELECT * FROM employees;