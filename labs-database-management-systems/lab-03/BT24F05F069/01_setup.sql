-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;

-- TODO: USE school_db;
USE school_db;

-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

CREATE TABLE employees (
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
('Rohan Sharma', 'SRE', 85000.00, '2023-01-15', ' 9876543210 '),
('Pankaj Karpe', 'SRE', 92000.50, '2024-03-10', '9123456780'),
('Meeran Khan', 'DevOps', 78000.00, '2025-11-20', ' 8888877777'),
('Anant Patil', 'QA', 65000.00, '2022-06-05', '7766554433 '),
('Sarah Chen', 'DevOps', 81000.00, '2026-02-01', ' 9900990099 ');

-- TODO: SELECT * FROM employees;
SELECT * FROM employees;
