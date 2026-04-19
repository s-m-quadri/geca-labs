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
('Alice Johnson', 'HR', 55000.00, '2020-01-15', ' 555-1234 '),
('Bob Smith', 'IT', 75000.00, '2019-03-22', '555-5678'),
('Charlie Brown', 'Finance', 65000.00, '2021-07-30', ' 555-8765'),
('Diana Prince', 'HR', 60000.00, '2018-11-05', '555-4321'),
('Ethan Hunt', 'IT', 80000.00, '2022-02-10', ' 555-3456 ');
 

-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

SELECT * FROM employees;
