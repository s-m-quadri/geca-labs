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

-- Drop database if it already exists (clean start)
DROP DATABASE IF EXISTS school_db;

-- Create database
CREATE DATABASE school_db;

-- Use the database
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

-- Insert sample data (with variation + spaces in phone)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Alice Johnson', 'HR', 45000.00, '2022-01-15', ' 9876543210'),
('Bob Smith', 'IT', 60000.50, '2021-06-20', '9123456780 '),
('Charlie Brown', 'Finance', 55000.75, '2023-03-10', ' 9988776655 '),
('Diana Prince', 'IT', 70000.00, '2020-11-05', '9012345678'),
('Eve Adams', 'HR', 48000.25, '2022-09-25', ' 9090909090');

-- View all data
SELECT * FROM employees;