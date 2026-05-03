-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).
 
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


INSERT INTO employees(full_name, dept, salary, hire_date, phone)VALUES
('Alice Johnson', 'Engineering', 85000.00, '2022-03-15', ' 123-456-7890'),
('Bob Smith', 'Marketing', 62000.50, '2021-07-22', '987-654-3210 '),
('Charlie Brown', 'HR', 55000.00, '2023-01-10', ' 555-0199 '),
('Diana Prince', 'Engineering', 92000.00, '2020-11-05', '444-555-6666'),
('Ethan Hunt', 'Operations', 75000.75, '2022-09-30', ' 222-333-4444 ');

-- TODO:
 SELECT * FROM employees;



