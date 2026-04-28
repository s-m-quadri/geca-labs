-- Lab 5-v2 -- procedural SQL (PostgreSQL): schema
-- Run: sudo -u postgres psql -f 01_setup.sql

DROP DATABASE IF EXISTS proc_lab;
CREATE DATABASE proc_lab;
-- \c proc_lab

CREATE TABLE accounts (
  id      SERIAL PRIMARY KEY,
  holder  VARCHAR(60) NOT NULL,
  balance DECIMAL(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE payroll (
  emp_id          SERIAL PRIMARY KEY,
  name            VARCHAR(60) NOT NULL,
  salary          DECIMAL(12,2) NOT NULL,
  bonus_eligible  BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO accounts (holder, balance) VALUES
  ('Alice', 1200.00),
  ('Bob',   450.50),
  ('Chen',  2000.00);

INSERT INTO payroll (name, salary, bonus_eligible) VALUES
  ('Ada', 50000.00, TRUE),
  ('Ben', 48000.00, FALSE),
  ('Cal', 52000.00, TRUE);

SELECT 'proc_lab ready' AS status;
