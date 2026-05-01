-- Task 4: Add Column
-- Add a 'grade' column (VARCHAR(10)) to students table

USE school_db;

ALTER TABLE students
ADD COLUMN grade VARCHAR(10);
