-- Lab 1: DDL Commands - advanced_ddl.sql
-- Task: Practice complex DDL operations

USE college_db;

-- TODO: Create faculty table with the following:
--   - faculty_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - employee_id (VARCHAR(10) NOT NULL UNIQUE)
--   - first_name (VARCHAR(50) NOT NULL)
--   - last_name (VARCHAR(50) NOT NULL)
--   - email (VARCHAR(100) NOT NULL UNIQUE)
--   - phone (VARCHAR(15))
--   - hire_date (DATE NOT NULL)
--   - department_id (INT)
--   - salary (DECIMAL(10, 2))
--   - office_number (VARCHAR(20))
-- Add CHECK constraints:
--   - employee_id must match pattern '^EMP[0-9]{6}$'
--   - salary between 30000 and 200000
--   - hire_date <= CURRENT_DATE
-- Add FOREIGN KEY for department_id with ON DELETE RESTRICT




-- TODO: Create class_schedule table with composite primary key:
--   - course_id (INT)
--   - faculty_id (INT)
--   - semester (VARCHAR(20))
--   - year (INT)
--   - room_number (VARCHAR(10))
--   - day_of_week (ENUM: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
--   - start_time (TIME)
--   - end_time (TIME)
-- Composite PRIMARY KEY on (course_id, faculty_id, semester, year)
-- FOREIGN KEYs for course_id and faculty_id with ON DELETE CASCADE
-- CHECK constraints: start_time < end_time, year BETWEEN 2020 AND 2030




-- TODO: Create student_performance table with generated columns:
--   - student_id (INT PRIMARY KEY)
--   - midterm_marks (DECIMAL(5, 2))
--   - final_marks (DECIMAL(5, 2))
--   - assignment_marks (DECIMAL(5, 2))
--   - total_marks (DECIMAL(5, 2)) - Generated as sum of all marks, STORED
--   - percentage (DECIMAL(5, 2)) - Generated as average, STORED
-- FOREIGN KEY for student_id with ON DELETE CASCADE




-- TODO: Create student_attendance table with partitioning:
--   - attendance_id (INT AUTO_INCREMENT)
--   - student_id (INT)
--   - course_id (INT)
--   - attendance_date (DATE)
--   - status (ENUM: 'Present', 'Absent', 'Late')
--   - remarks (TEXT)
-- PRIMARY KEY (attendance_id, attendance_date)
-- FOREIGN KEY for student_id
-- PARTITION BY RANGE (YEAR(attendance_date)) with partitions:
--   - p2023 VALUES LESS THAN (2024)
--   - p2024 VALUES LESS THAN (2025)
--   - p2025 VALUES LESS THAN (2026)
--   - p_future VALUES LESS THAN MAXVALUE




-- TODO: Create a VIEW called student_details that shows:
--   - student_id
--   - full_name (concatenation of first_name and last_name)
--   - email
--   - gpa
--   - department_name
-- Use LEFT JOIN with departments




-- TODO: Show all views in the database


-- TODO: Describe the student_details view


-- TODO: Query information_schema to show all constraints in college_db


-- TODO: Query information_schema to show all foreign key relationships


-- TODO: Query information_schema to show all indexes in college_db

