Task 1: Setup database and employees table
You need sample data for later tasks (at least 5 rows, 2+ departments).

  DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

  USE school_db;

  CREATE TABLE employees with:
  emp_id INT PRIMARY KEY AUTO_INCREMENT
  full_name VARCHAR(60) NOT NULL
  dept VARCHAR(40)
  salary DECIMAL(10,2)
  hire_date DATE
  phone VARCHAR(25)

  INSERT at least 5 rows. Vary dept, salary, hire_date.
Optional: put leading/trailing spaces in some phone values for TRIM task later.

SELECT * FROM employees;


-- Drop and create database
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

-- Insert sample data (with varied departments and salaries)
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'HR', 45000.50, '2022-03-15', ' 9876543210'),
('Neha Verma', 'IT', 62000.75, '2021-07-10', '9123456780 '),
('Raj Patel', 'Finance', 55000.00, '2020-01-20', ' 9988776655 '),
('Sneha Iyer', 'IT', 72000.25, '2019-11-05', '9090909090'),
('Arjun Singh', 'HR', 48000.80, '2023-06-01', ' 9012345678');

-- View data
SELECT * FROM employees;