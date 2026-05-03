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
-- Drop and create database
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

-- Insert sample data (5+ rows, multiple departments)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'IT', 50000.00, '2022-01-15', ' 9876543210 '),
('Priya Verma', 'HR', 45000.00, '2021-03-10', '9123456780'),
('Rahul Patil', 'Finance', 60000.00, '2020-07-22', ' 9988776655'),
('Sneha Kulkarni', 'IT', 55000.00, '2023-05-18', '8899001122 '),
('Vikas Singh', 'HR', 48000.00, '2019-11-30', ' 9012345678 '),
('Neha Joshi', 'Finance', 62000.00, '2022-09-12', '9988007766');

-- View all data
SELECT * FROM employees;