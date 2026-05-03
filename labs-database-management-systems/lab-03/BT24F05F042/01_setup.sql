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
-- Create database
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;
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

-- Insert at least 5 rows
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'HR', 35000.50, '2022-01-15', ' 987654321'),
('Neha Verma', 'IT', 55000.00, '2021-06-20', '912345678 '),
('Raj Patel', 'Finance', 45000.75, '2020-03-10', ' 998877665 '),
('Sneha Iyer', 'IT', 60000.00, '2023-02-01', '987123456'),
('Karan Mehta', 'Sales', 30000.25, '2022-11-05', ' 909090909');

-- Display data
SELECT * FROM employees;
