--- Lab 4 — Task 1: Schema + Seed Data for JOIN Practice

-- Reset (safe rerun)
DROP DATABASE IF EXISTS lab4_db;
CREATE DATABASE lab4_db;
USE lab4_db;

-- =====================
-- Tables
-- =====================

-- Departments
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
);

-- Employees
CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  dept_id INT,
  salary DECIMAL(10,2),
  manager_id INT,
  hire_date DATE,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
  FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- Projects
CREATE TABLE projects (
  proj_id INT PRIMARY KEY,
  proj_name VARCHAR(100) NOT NULL,
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Employee ↔ Project mapping (many-to-many)
CREATE TABLE employee_projects (
  emp_id INT,
  proj_id INT,
  role VARCHAR(50),
  PRIMARY KEY (emp_id, proj_id),
  FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
  FOREIGN KEY (proj_id) REFERENCES projects(proj_id)
);

-- =====================
-- Seed Data
-- =====================

-- Departments
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Sales'),
(4, 'Finance');

-- Employees
INSERT INTO employees VALUES
(101, 'Amit Sharma', 2, 60000, NULL, '2020-01-15'),
(102, 'Neha Verma', 2, 55000, 101, '2021-03-10'),
(103, 'Ravi Kumar', 3, 45000, NULL, '2019-07-23'),
(104, 'Sneha Patil', 1, 40000, NULL, '2022-05-01'),
(105, 'Vikram Singh', 3, 47000, 103, '2020-11-12'),
(106, 'Anjali Mehta', 4, 52000, NULL, '2018-09-30'),
(107, 'Karan Gupta', NULL, 38000, NULL, '2023-01-01'); -- no dept (for LEFT JOIN puzzles)

-- Projects
INSERT INTO projects VALUES
(201, 'Website Revamp', 2),
(202, 'Sales Dashboard', 3),
(203, 'Recruitment Drive', 1),
(204, 'Budget Planning', 4),
(205, 'AI Prototype', 2);

-- Employee-Project Mapping
INSERT INTO employee_projects VALUES
(101, 201, 'Lead'),
(102, 201, 'Developer'),
(102, 205, 'Developer'),
(103, 202, 'Lead'),
(105, 202, 'Sales Exec'),
(104, 203, 'Coordinator'),
(106, 204, 'Analyst');

-- =====================
-- Optional sanity checks
-- =====================
-- SHOW TABLES;
-- SELECT * FROM employees;
-- SELECT * FROM departments;
-- SELECT * FROM projects;
-- SELECT * FROM employee_projects;
