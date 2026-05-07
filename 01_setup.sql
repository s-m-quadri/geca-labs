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

-- TODO: SELECT * FROM employees;

DROP DATABASE IF EXISTS school_db;
CREATE DATABASE IF NOT EXISTS school_db;
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
('Mayur Wakchaure', 'HR', 120000.00, '2005-06-13', '   9850064866'),
('Anushka Satpute', 'HR', 100000.00, '2006-03-11', '   9850062353'),
('Pawan Pawar', 'PR', 135000.00, '2010-01-20', '8888877777'),
('Rohan Pawar', 'CR', 95000.00, '2015-11-15', '7777766666'),  
('Harsh Tiwari', 'CR', 200000.00, '2003-03-13', '   9850012345'),
('Mangesh Wagh', 'CR', 200000.00, '2005-04-01', '   9850123445');

SELECT * FROM employees;