-- Lab 4 — Task 1: schema and seed data for join practice + puzzles
-- Run: sudo mysql < 01_setup.sql

-- Lab 4 — Task 1: schema and seed data for join practice + puzzles
-- Run: sudo mysql < 01_setup.sql

-- Create database
-- Lab 4 — Task 1: schema and seed data for join practice + puzzles
-- Run: sudo mysql < 01_setup.sql

-- Create database
DROP DATABASE IF EXISTS join_lab;
CREATE DATABASE join_lab;
USE join_lab;

-- Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL
);

-- Staff table
CREATE TABLE staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    dept_id INT,
    join_date DATE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Project-Staff mapping table
CREATE TABLE project_staff (
    project_id INT,
    staff_id INT,
    hours INT,
    PRIMARY KEY (project_id, staff_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- Seed data
INSERT INTO departments (dept_name) VALUES
('Computer Science'),
('Mechanical'),
('Electrical'),
('Civil');

INSERT INTO staff (name, dept_id, join_date) VALUES
('Alice', 1, '2020-01-15'),
('Bob', 1, '2021-03-10'),
('Charlie', 2, '2019-07-20'),
('David', 3, '2022-11-05'),
('Eva', NULL, '2021-06-30'); -- staff without department

INSERT INTO projects (title, dept_id) VALUES
('AI Research', 1),
('Robotics', 2),
('Power Systems', 3),
('Bridge Design', 4);

INSERT INTO project_staff (project_id, staff_id, hours) VALUES
(1, 1, 40),
(1, 2, 30),
(2, 3, 25),
(3, 4, 50),
(4, 1, 10);
