-- Task 1: Setup database and employees table

-- DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;

-- USE school_db;
USE school_db;

-- CREATE TABLE employees
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
);

-- INSERT at least 5 rows with varying data
-- Note: Included leading/trailing spaces in phone numbers for later TRIM exercises
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES 
('Alice Johnson', 'Engineering', 85000.00, '2022-03-15', ' 555-0101'),
('Bob Smith', 'Human Resources', 62000.50, '2021-11-10', '555-0102 '),
('Charlie Davis', 'Engineering', 92000.00, '2023-01-20', '  555-0103'),
('Diana Prince', 'Marketing', 75000.00, '2020-05-05', '555-0104'),
('Evan Wright', 'Marketing', 71000.75, '2022-08-12', ' 555-0105 ');

-- SELECT * FROM employees;
SELECT * FROM employees;