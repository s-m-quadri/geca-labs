-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

DROP DATABASE IF EXISTS school_db;
 CREATE DATABASE school_db;

USE school_db;

 CREATE TABLE employees(
 emp_id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(60) NOT NULL,
  dept VARCHAR(40),
 salary DECIMAL(10,2),
 hire_date DATE,
 phone VARCHAR(25));

INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Alice Johnson', 'Engineering', 85000.00, '2022-03-15', ' 555-0101 '),
('Bob Smith', 'Marketing', 62500.50, '2021-06-22', '555-0102'),
('Charlie Brown', 'Engineering', 91000.00, '2020-11-05', ' 555-0103'),
('Diana Prince', 'HR', 58000.00, '2023-01-10', '555-0104 '),
('Edward Norton', 'Sales', 72000.75, '2019-08-30', ' 555-0105 ');
 SELECT * FROM employees;



