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
('Neha Patil', 'HR', 45000.00, '2021-03-10', '9123456789'),
('Rahul Deshmukh', 'Finance', 60000.00, '2020-11-25', ' 9988776655'),
('Priya Kulkarni', 'IT', 70000.00, '2023-01-05', '8899001122'),
('Suresh Jadhav', 'Sales', 40000.00, '2022-09-18', ' 9012345678 ');

SELECT * FROM employees;