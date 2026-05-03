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
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
('Alice Johnson', 'HR', 55000.00, '2018-03-15', ' 123-456-7890 '),
('Bob Smith', 'IT', 75000.50, '2019-07-22', '987-654-3210'),
('Charlie Brown', 'Finance', 62000.75, '2020-01-10', '555-123-4567'),
('Diana Prince', 'HR', 58000.25, '2017-11-05', '444-555-6666'),
('Ethan Hunt', 'IT', 80000.00, '2021-05-30', '333-444-5555');



