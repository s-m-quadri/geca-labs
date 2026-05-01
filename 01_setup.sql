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

INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Aarav Shah', 'IT', 51000.00, '2021-04-12', ' 98765 43210 '),
('Nisha Patel', 'HR', 32000.00, '2022-08-01', ' 91234 56789'),
('Imran Khan', 'Sales', 39000.00, '2020-11-15', '99887 77665 '),
('Meera Iyer', 'IT', 42000.00, '2019-06-20', ' 90909 90909 '),
('Rohan Desai', 'Finance', 47000.00, '2023-01-10', '90123 45678'),
('Sara Ali', 'Sales', 36000.00, '2024-03-05', ' 88000 11223 ');

SELECT * FROM employees;
