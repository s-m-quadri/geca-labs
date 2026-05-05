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
-- Task 1: Setup database and employees table

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
('Amit Sharma', 'IT', 55000.00, '2022-06-15', ' 9876543210 '),
('Priya Patil', 'HR', 48000.00, '2021-03-10', '9123456780'),
('Rahul Verma', 'Finance', 62000.00, '2020-11-25', ' 9988776655'),
('Sneha Deshmukh', 'IT', 70000.00, '2019-07-01', '8899001122 '),
('Vikas Jadhav', 'Marketing', 45000.00, '2023-01-05', ' 7766554433 ');

SELECT * FROM employees;