-- Task 4: Add Column
-- Add a 'grade' column (VARCHAR(10)) to students table

USE school_db;

-- TODO: Write your ALTER TABLE ADD COLUMN command here
ALTER TABLE students ADD COLUMN grade VARCHAR(10);
SELECT * FROM students; -- This line is just to verify the column addition, you can remove