-- Lab 1: DDL Commands - alter_table.sql
-- Task: Modify table structures using ALTER TABLE

USE college_db;

-- TODO: Add a new column 'address' (TEXT) to the students table


-- TODO: Add a new column 'gpa' (DECIMAL(3, 2), DEFAULT 0.00) to students table
-- Include CHECK constraint: gpa BETWEEN 0.00 AND 4.00


-- TODO: Modify the 'phone' column in students table to VARCHAR(20)


-- TODO: Change the column name 'date_of_birth' to 'dob' in students table


-- TODO: Add FOREIGN KEY constraint to students table
-- Link department_id to departments(department_id) with ON DELETE SET NULL and ON UPDATE CASCADE


-- TODO: Drop the 'address' column from students table


-- TODO: Add an INDEX on 'last_name' column in students table (name it idx_last_name)


-- TODO: Add a composite INDEX on students (student_id, course_id) in enrollments table


-- TODO: Add UNIQUE constraint on 'head_of_department' in departments table


-- TODO: Drop the UNIQUE constraint on 'head_of_department'


-- TODO: Rename the enrollments table to 'student_enrollments'


-- TODO: Rename it back to 'enrollments'


-- TODO: Display the modified structure of students table


-- TODO: Display all indexes on students table

