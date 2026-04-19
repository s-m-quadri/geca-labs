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
-- Drop database if it exists and create a new one
DROP DATABASE IF EXISTS school_db;
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

-- Insert sample data
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Rohit Kumar', 'IT', 60000.00, '2022-02-10', ' 9876501234'),
('Anjali Deshmukh', 'HR', 42000.50, '2021-05-18', '9123456789 '),
('Karan Singh', 'Finance', 50000.75, '2020-09-25', ' 9988776655 '),
('Meena Joshi', 'IT', 65000.00, '2023-01-12', '9012345678'),
('Suresh Patil', 'HR', 38000.00, '2019-07-30', ' 9090909090');

-- Display all records
SELECT * FROM employees;