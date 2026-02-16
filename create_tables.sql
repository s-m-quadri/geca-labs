-- Lab 1: DDL Commands - create_tables.sql
-- Task: Create tables with proper constraints

USE college_db;

-- TODO: Create departments table with the following columns:
--   - department_id (INT, PRIMARY KEY, AUTO_INCREMENT)
--   - department_name (VARCHAR(100), NOT NULL, UNIQUE)
--   - head_of_department (VARCHAR(100))
--   - building (VARCHAR(50))
--   - budget (DECIMAL(12, 2), DEFAULT 0.00)
-- Add CHECK constraint: budget >= 0




-- TODO: Create students table with the following columns:
--   - student_id (INT, PRIMARY KEY, AUTO_INCREMENT)
--   - first_name (VARCHAR(50), NOT NULL)
--   - last_name (VARCHAR(50), NOT NULL)
--   - email (VARCHAR(100), UNIQUE, NOT NULL)
--   - phone (VARCHAR(15))
--   - date_of_birth (DATE)
--   - enrollment_date (DATE, DEFAULT CURRENT_DATE)
--   - department_id (INT)
-- Add CHECK constraint: email must contain '@' and '.'




-- TODO: Create courses table with the following columns:
--   - course_id (INT, PRIMARY KEY, AUTO_INCREMENT)
--   - course_code (VARCHAR(10), NOT NULL, UNIQUE)
--   - course_name (VARCHAR(150), NOT NULL)
--   - credits (INT, NOT NULL, DEFAULT 3)
--   - department_id (INT)
-- Add CHECK constraint: credits BETWEEN 1 AND 6
-- Add FOREIGN KEY: department_id references departments(department_id) with ON DELETE SET NULL and ON UPDATE CASCADE




-- TODO: Create enrollments table with the following columns:
--   - enrollment_id (INT, PRIMARY KEY, AUTO_INCREMENT)
--   - student_id (INT, NOT NULL)
--   - course_id (INT, NOT NULL)
--   - enrollment_date (DATE, DEFAULT CURRENT_DATE)
--   - grade (CHAR(2))
--   - status (ENUM: 'Active', 'Completed', 'Dropped', DEFAULT 'Active')
-- Add FOREIGN KEYs for student_id and course_id with ON DELETE CASCADE
-- Add CHECK constraint: grade IN ('A+', 'A', 'B+', 'B', 'C', 'D', 'F')




-- TODO: Display all tables created (use SHOW TABLES)


-- TODO: Display structure of each table (use DESCRIBE for each table)



