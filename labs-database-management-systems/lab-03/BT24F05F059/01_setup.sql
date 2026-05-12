DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;
USE school_db;
 
CREATE TABLE employees (
    emp_id    INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept      VARCHAR(30) NOT NULL,
    salary    DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    phone     VARCHAR(20)
);
 
INSERT INTO employees (full_name, dept, salary, hire_date, phone) VALUES
    ('Alice Smith',   'Engineering', 55000, '2020-03-15', '9876543210'),
    ('Bob Jones',     'Engineering', 48000, '2019-06-01', ' 9123456789 '),
    ('Carol Lee',     'HR',          42000, '2021-01-10', '8001234567'),
    ('David Kim',     'HR',          38000, '2022-07-22', '8009876543'),
    ('Eve Patel',     'Engineering', 61000, '2018-11-05', '9001112233');