-- Lab 2: DML Commands - setup.sql
-- Task: Create database and tables for DML practice

-- TODO: Drop college_db if it exists


-- TODO: Create college_db database


-- TODO: Use college_db


-- TODO: Create departments table with:
--   - department_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - department_name (VARCHAR(100) NOT NULL UNIQUE)
--   - building (VARCHAR(50))
--   - budget (DECIMAL(12, 2) DEFAULT 0.00)




-- TODO: Create students table with:
--   - student_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - first_name (VARCHAR(50) NOT NULL)
--   - last_name (VARCHAR(50) NOT NULL)
--   - email (VARCHAR(100) UNIQUE NOT NULL)
--   - phone (VARCHAR(15))
--   - dob (DATE)
--   - enrollment_date (DATE DEFAULT CURRENT_DATE)
--   - department_id (INT)
--   - gpa (DECIMAL(3, 2) DEFAULT 0.00)
--   - FOREIGN KEY for department_id




-- TODO: Create courses table with:
--   - course_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - course_code (VARCHAR(10) NOT NULL UNIQUE)
--   - course_name (VARCHAR(150) NOT NULL)
--   - credits (INT NOT NULL DEFAULT 3)
--   - department_id (INT)
--   - FOREIGN KEY for department_id




-- TODO: Create enrollments table with:
--   - enrollment_id (INT PRIMARY KEY AUTO_INCREMENT)
--   - student_id (INT NOT NULL)
--   - course_id (INT NOT NULL)
--   - enrollment_date (DATE DEFAULT CURRENT_DATE)
--   - grade (CHAR(2))
--   - status (ENUM: 'Active', 'Completed', 'Dropped', DEFAULT 'Active')
--   - FOREIGN KEYs for student_id and course_id with ON DELETE CASCADE




-- TODO: Show all created tables

