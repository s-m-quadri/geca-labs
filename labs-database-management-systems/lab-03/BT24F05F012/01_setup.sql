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
('John Doe', 'IT', 45000.00, '2020-01-15', '123-456-7890'),
('Jane Smith', 'HR', 35000.00, '2019-05-20', ' 987-654-3210 '),
('Bob Johnson', 'Finance', 55000.00, '2021-03-10', '555-123-4567'),
('Alice Brown', 'IT', 48000.00, '2022-07-25', ' 111-222-3333 '),
('Charlie Wilson', 'Marketing', 40000.00, '2018-11-30', '444-555-6666');

SELECT * FROM employees;
