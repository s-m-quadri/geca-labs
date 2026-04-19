-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: 
DROP DATABASE IF EXISTS school_db; 
CREATE DATABASE school_db;

-- TODO:
 USE school_db;

-- TODO:
 CREATE TABLE employees(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
 );
-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Amit Sharma', 'HR', 35000.00, '2022-01-15', ' 9876543210'),
('Priya Singh', 'IT', 55000.00, '2021-07-20', '9876501234 '),
('Rahul Verma', 'Finance', 48000.00, '2020-03-10', ' 9123456789 '),
('Sneha Patil', 'IT', 60000.00, '2023-05-01', '9988776655'),
('Vikram Joshi', 'HR', 42000.00, '2019-11-25', ' 9090909090');

-- TODO: 
SELECT * FROM employees;
