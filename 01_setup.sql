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


USE school_db;


CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
);


INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Anisha Patil', 'HR', 45000.00, '2022-03-15', ' 9876543210 '),
('Rahul Sharma', 'IT', 60000.50, '2021-07-20', '9123456780'),
('Priya Deshmukh', 'Finance', 55000.75, '2023-01-10', ' 9988776655'),
('Amit Verma', 'IT', 72000.00, '2020-11-05', '9876501234 '),
('Sneha Kulkarni', 'HR', 48000.25, '2022-08-25', ' 9012345678')
SELECT * FROM employees;
