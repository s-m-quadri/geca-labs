-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

-- TODO: USE school_db;

-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

-- TODO: SELECT * FROM employees;

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

INSERT INTO employees(full_name,dept,salary,hire_date,phone) VALUES
('Vedant Dakare','CSE',50000.00,'2026-05-24',' 123-456-7890 '),
('Anjali Sharma','ECE',55000.00,'2025-03-15','987-654-3210'),
('Rohit Verma','CSE',60000.00,'2024-01-10',' 555-555-5555 '),
('Priya Singh','ME',45000.00,'2023-07-20','444-444-4444'),
('Amit Patel','ECE',52000.00,'2022-11-05','333-333-3333');

SELECT * FROM employees;