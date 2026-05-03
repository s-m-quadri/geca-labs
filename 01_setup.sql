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

CREATE TABLE employees(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10, 2),
    hire_date DATE,
    phone VARCHAR(25)
);

INSERT INTO employees(dept, full_name, salary, hire_date)
VALUE 
('Sales', 'Meeran Shaikh', 12000.00, '2026-04-01'),
('IT', 'Krutarth Fulare' , 200000.00, '2026-01-01'),
('Marketing', 'Prabhat Jha' , 22000.00, '2026-02-01'),
('Security', 'Tanmay Kolhe' ,150000.00, '2025-12-01'),
('Hospitatlity', 'Sarthak Deshmukh' ,19900.00, '2025-11-01');

SELECT * FROM employees;
