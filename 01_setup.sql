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

INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
    ('<name1>', '<dept1>', <salary1>, '<yyyy-mm-dd>', ' <phone1> '),
    ('<name2>', '<dept2>', <salary2>, '<yyyy-mm-dd>', '<phone2>'),
    ('<name3>', '<dept1>', <salary3>, '<yyyy-mm-dd>', '  <phone3>'),
    ('<name4>', '<dept3>', <salary4>, '<yyyy-mm-dd>', '<phone4>  '),
    ('<name5>', '<dept2>', <salary5>, '<yyyy-mm-dd>', '<phone5>');

SELECT * FROM employees;