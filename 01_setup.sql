-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

-- TODO: USE school_db;
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;
-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

USE school_db;
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
('Akshada Mane', 'IT', 45000.75, '2022-06-15', ' 9876543210 '),
('Rahul Patil', 'HR', 38000.50, '2021-03-10', '9123456780'),
('Sneha Joshi', 'Finance', 52000.00, '2020-11-25', ' 9988776655'),
('Amit Sharma', 'IT', 47000.25, '2023-01-05', '9090909090 '),
('Pooja Deshmukh', 'Marketing', 41000.80, '2022-09-18', ' 9012345678 ');
-- TODO: SELECT * FROM employees;
SELECT * FROM employees;
