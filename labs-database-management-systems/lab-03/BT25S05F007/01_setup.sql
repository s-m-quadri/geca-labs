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

-- Insert sample data (at least 5 rows, multiple departments)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'IT', 65000.00, '2022-06-15', ' 9876543210 '),
('Neha Patil', 'HR', 52000.00, '2021-03-10', '9123456780'),
('Ravi Kumar', 'Finance', 72000.00, '2020-11-25', ' 9988776655'),
('Sneha Joshi', 'IT', 68000.00, '2023-01-05', '9012345678 '),
('Vikram Desai', 'Sales', 50000.00, '2019-07-18', '8899001122');

-- View all employees
SELECT * FROM employees;