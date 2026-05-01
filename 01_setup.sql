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
('Amit Sharma', 'HR', 30000.00, '2021-06-15', ' 9876543210 '),
('Neha Patil', 'IT', 45000.00, '2020-03-10', '9123456780'),
('Rahul Verma', 'Finance', 50000.00, '2019-11-25', ' 9988776655'),
('Sneha Kulkarni', 'IT', 42000.00, '2022-01-05', '9012345678 '),
('Vikram Singh', 'HR', 35000.00, '2021-09-18', ' 9090909090');

-- Display all records
SELECT * FROM employees;