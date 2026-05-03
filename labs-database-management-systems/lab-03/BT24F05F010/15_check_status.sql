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
                                                    