-- Task 9: Drop Table
-- Drop (delete) the students table

USE school_db;

-- TODO: Write your DROP TABLE command here
-- Warning: This will permanently delete the table!
DROP TABLE students;
-- To verify the table has been dropped, you can try to select from it (this should give an error)
SELECT * FROM students; -- This should result in an error since the table no longer exists