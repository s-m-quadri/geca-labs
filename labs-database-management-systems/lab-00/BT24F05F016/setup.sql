-- Lab 0: Database Setup
-- Task: Create a database named "student_db" and use it
-- Purpose: Initialize database for DBMS lab experiments
-- Date: 2026-05-01

-- TODO: Complete the following

-- Step 1: Create database
CREATE DATABASE IF NOT EXISTS student_db;
SHOW DATABASES;

-- Step 2: Use the database
USE student_db;

-- Step 3: Display current database
SELECT DATABASE() AS 'Current Database';
SELECT 'Database setup completed successfully!' AS Status;
