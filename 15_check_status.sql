-- Show all databases
SHOW DATABASES;

-- Switch to database
USE school_db;

-- Show all tables
SHOW TABLES;

-- Show structure of employees table
DESCRIBE employees;

-- Total number of employees
SELECT COUNT(*) AS total_employees
FROM employees;

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