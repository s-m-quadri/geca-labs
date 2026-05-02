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
('Arjun Sharma', 'CSE', 75000.00, '2022-03-15', ' 9876543210 '),
('Priya Patil', 'IT', 62000.50, '2021-11-20', '8765432109'),
('Rohan Deshmukh', 'CSE', 55000.00, '2023-01-10', ' 7654321098'),
('Anjali Gupta', 'HR', 48000.75, '2020-05-25', '6543210987 '),
('Siddharth Malhotra', 'IT', 68000.00, '2022-08-12', ' 9988776655 ');

SELECT * FROM employees;