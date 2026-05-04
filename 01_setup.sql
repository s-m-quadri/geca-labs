
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
  ('Ravi Sharma', 'Sales', 52000.00, '2022-08-10', ' 9876543210'),
  ('Nisha Patel', 'HR', 61000.00, '2023-02-05', '9876501234 '),
  ('Arjun Desai', 'IT', 72000.00, '2021-11-20', '9988776655'),
  ('Meera Rao', 'Marketing', 58000.00, '2024-01-12', ' 9123456789'),
  ('Sana Sheikh', 'Finance', 64000.00, '2022-05-03', '9034567890 ');
SELECT * FROM employees;