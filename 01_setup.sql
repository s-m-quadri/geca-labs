-- Lab 4 — Task 1: schema and seed data for join practice + puzzles
-- Run: sudo mysql < 01_setup.sql


DROP DATABASE IF EXISTS join_lab;
CREATE DATABASE join_lab;
USE join_lab;

CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(40) NOT NULL,
  floor_no INT NOT NULL
);

CREATE TABLE staff (
  staff_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(60) NOT NULL,
  dept_id INT NOT NULL,
  joined_on DATE NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE projects (
  proj_id INT PRIMARY KEY,
  title VARCHAR(80) NOT NULL,
  dept_id INT NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE project_staff (
  staff_id INT NOT NULL,
  proj_id INT NOT NULL,
  hours INT NOT NULL DEFAULT 0,
  PRIMARY KEY (staff_id, proj_id),
  FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
  FOREIGN KEY (proj_id) REFERENCES projects(proj_id)
);

INSERT INTO departments (dept_id, dept_name, floor_no) VALUES
  (1, 'Logic', 2),
  (2, 'Systems', 2),
  (3, 'Data', 4),
  (4, 'Idle', 1);

INSERT INTO staff (name, dept_id, joined_on) VALUES
  ('Ada', 1, '2019-03-01'),
  ('Bob', 1, '2020-06-15'),
  ('Chen', 2, '2018-01-10'),
  ('Dina', 2, '2021-09-01'),
  ('Eve', 3, '2017-11-20'),
  ('Finn', 3, '2022-02-28');


INSERT INTO projects (proj_id, title, dept_id) VALUES
  (101, 'Riddle-UI', 1),
  (102, 'Riddle-API', 1),
  (201, 'Kernel', 2),
  (301, 'Warehouse', 3);


INSERT INTO project_staff (staff_id, proj_id, hours) VALUES
  (1, 101, 10), (1, 102, 5),
  (2, 101, 8),
  (3, 201, 40),
  (4, 201, 10),
  (5, 301, 30), (5, 201, 5),
  (6, 301, 20);

SELECT 'join_lab ready' AS status;


