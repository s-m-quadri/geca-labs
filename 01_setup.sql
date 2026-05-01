-- Lab 5 — procedural SQL (MySQL stored programs): schema
-- Run: sudo mysql < 01_setup.sql

DROP DATABASE IF EXISTS proc_lab;
CREATE DATABASE proc_lab;
USE proc_lab;

CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  holder VARCHAR(60) NOT NULL,
  balance DECIMAL(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE payroll (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(60) NOT NULL,
  salary DECIMAL(12,2) NOT NULL,
  bonus_eligible TINYINT(1) NOT NULL DEFAULT 0
);

INSERT INTO accounts (holder, balance) VALUES
  ('Alice', 1200.00),
  ('Bob', 450.50),
  ('Chen', 2000.00);

INSERT INTO payroll (name, salary, bonus_eligible) VALUES
  ('Ada', 50000.00, 1),
  ('Ben', 48000.00, 0),
  ('Cal', 52000.00, 1);

SELECT 'proc_lab ready' AS status;


