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
CREATE DATABASE IF NOT EXISTS school_db;
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
('Mayur Wakchaure', 'HR', 120000.00, '2005-06-13', '   9850064866'),
('Anushka Satpute', 'HR', 100000.00, '2006-03-11', '   9850062353'),
('Pawan Pawar', 'PR', 135000.00, '2010-01-20', '8888877777'),
('Rohan Pawar', 'CR', 95000.00, '2015-11-15', '7777766666'),  
('Harsh Tiwari', 'CR', 200000.00, '2003-03-13', '   9850012345'),
('Mangesh Wagh', 'CR', 200000.00, '2005-04-01', '   9850123445');

SELECT * FROM employees;