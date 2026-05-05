-- Task 4: Add Column
-- Add a 'grade' column (VARCHAR(10)) to students table

USE school_db;
ALTER TABLE students
ADD COLUMN email VARCHAR(100);
 
ALTER TABLE students
ADD COLUMN phone VARCHAR(15);
 
DESCRIBE students;

-- TODO: Write your ALTER TABLE ADD COLUMN command here
