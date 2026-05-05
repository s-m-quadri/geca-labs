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
CREATE DATABASE IF NOT EXISTS school_db;
USE school_db;
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
);
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Alice Johnson', 'HR', 55000.00, '2018-03-15', ' 555-1234 '),
('Bob Smith', 'Engineering', 75000.00, '2019-07-22', '555-5678'),
('Charlie Davis', 'Marketing', 60000.00, '2020-01-10', ' 555-8765'),
('Diana Evans', 'Engineering', 80000.00, '2017-11-05', '555-4321'),
('Ethan Brown', 'HR', 52000.00, '2021-06-30', ' 555-6789 ');
SELECT * FROM employees;

