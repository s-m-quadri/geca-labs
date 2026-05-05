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
  ('Aman Joshi', 'Sales', 45000.00, '2022-02-18', ' 9876543210'),
  ('Neha Patel', 'HR', 52000.00, '2021-07-10', '98765 43210 '),
  ('Ravi Kumar', 'Finance', 61000.50, '2020-11-05', ' 9123456789'),
  ('Sara Khan', 'Sales', 47000.00, '2023-01-25', '9988776655'),
  ('Priya Singh', 'IT', 58000.00, '2022-09-14', ' 9900112233 ');

SELECT * FROM employees;