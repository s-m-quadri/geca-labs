-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;
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

-- Insert sample data (with varied departments and some spaced phone values)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'HR', 45000.00, '2021-06-15', ' 9876543210'),
('Priya Verma', 'IT', 60000.50, '2020-03-10', '9123456780 '),
('Rohit Patil', 'Finance', 55000.75, '2019-11-25', ' 9988776655 '),
('Sneha Kulkarni', 'IT', 72000.00, '2022-01-05', '9090909090'),
('Vikram Deshmukh', 'HR', 48000.25, '2018-08-19', ' 9001122334');

-- View data
SELECT * FROM employees;
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
