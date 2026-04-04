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

INSERT INTO employees VALUES
(1, "Anand Kharat", "Finance", 5750.5, "2003-03-03", "12345 67890"),
(2, "Sarthak Jha", "Marketing", 3950.6, "2024-07-02", "098 765 4321"),
(3, "Ayaz Khan", "Marketing", 12000.0, "2022-06-01", " 567 384 0912"),
(4, "Aman Singh", "Finance", 2250.0, "2024-03-09", "0987 123 456"),
(5, "Anil Thakare", "Finance", 15550.5, "2020-01-06", "47928 52043");

-- TODO: SELECT * FROM employees;

SELECT * FROM employees;