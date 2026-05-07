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
  ('Asha Patel', 'Accounts', 45000.75, '2022-03-15', ' 9876512345'),
  ('Rahul Sharma', 'HR', 52000.50, '2021-08-01', '9876523456 '),
  ('Mira Iyer', 'Accounts', 39000.00, '2023-01-10', ' 9876534567 '),
  ('Sohail Khan', 'IT', 62000.25, '2020-11-20', '9876545678'),
  ('Priya Desai', 'HR', 41000.95, '2024-02-28', ' 9876556789'),
  ('Tanvi Rao', 'IT', 33500.10, '2023-09-05', '9876567890 '),
  ('Nikita Gupte', 'Support', 28000.00, '2024-04-30', ' 9876578901 ');

SELECT * FROM employees;
