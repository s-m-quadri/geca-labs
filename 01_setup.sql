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

create database if not exists school_db;
use school_db;
create table if not exists employees (
    emp_id int primary key auto_increment,
    full_name varchar(60) not null,
    dept varchar(40),
    salary decimal(10,2),
    hire_date date,
    phone varchar(25)
);

Insert into employees (full_name, dept, salary, hire_date, phone) values
('Alice Johnson', 'HR', 55000.00, '2018-03-15', ' 555-1234 '),
('Bob Smith', 'IT', 75000.00, '2019-07-22', '555-5678'),
('Charlie Brown', 'Finance', 65000.00, '2020-01-10', ' 555-8765'),
('Diana Prince', 'HR', 60000.00, '2017-11-05', '555-4321'),
('Ethan Hunt', 'IT', 80000.00, '2021-05-30', ' 555-6789 ');

select * from employees;



