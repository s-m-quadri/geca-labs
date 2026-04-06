-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

 DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

 USE school_db;
 CREATE TABLE employees (
   emp_id INT PRIMARY KEY AUTO_INCREMENT,
   full_name VARCHAR(60) NOT NULL,
   dept VARCHAR(40),
   salary DECIMAL(10,2),
   hire_date DATE
 );
 phone VARCHAR(25)

 INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

 SELECT * FROM employees;
