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

-- Drop and recreate the database
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

-- Insert sample data (5 rows, multiple departments, varied salaries/dates)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amruta Rothe', 'cse', 52000.00, '2025-03-15', ' 8485096264'),
('sakshi bhosale', 'IT', 68000.00, '2024-07-10', '9986704951'),
('komal kale', 'cse', 75000.00, '2014-11-05', '9123456789'),
('siya patil', 'IT', 64000.00, '2022-01-20', '9999396678'),
('sayali jadhav', 'entc', 59000.00, '2026-09-12', '555-678-9012');

-- View inserted data
SELECT * FROM employees;