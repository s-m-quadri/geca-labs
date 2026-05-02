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
("Aadarsh Charpe","CSE",40000,'2026-03-23','8007036685'),
("Vedant Dakare","IT",50000,'2026-04-20','  9834762293  '),
("Sudhanshu Bagde","HR",20000,'2026-03-15','9844762365'),
("Priya Sharma","IT",65000,'2025-06-10','  9123456789 '),
("Chaitanya Shah","HR",35000,'2025-11-05','9987654321');

SELECT * FROM employees;