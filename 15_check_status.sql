-- Task 15: Check Status
-- Inspect database state anytime

SHOW DATABASES;

USE school_db;

SHOW TABLES;

DESCRIBE employees;

SELECT COUNT(*) AS total_employees FROM employees;

SELECT * FROM employees;

SELECT dept, COUNT(*) AS n, SUM(salary) AS total_pay, AVG(salary) AS avg_pay
FROM employees
GROUP BY dept;
-- List all databases
SHOW DATABASES;

-- Switch to your database
USE school_db;

-- List tables in the database
SHOW TABLES;

-- Show structure of employees table
DESCRIBE employees;

-- Total number of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- View all employee data
SELECT * FROM employees;

-- Department-wise summary
SELECT 
    dept, 
    COUNT(*) AS n, 
    SUM(salary) AS total_pay, 
    AVG(salary) AS avg_pay
FROM employees
GROUP BY dept;