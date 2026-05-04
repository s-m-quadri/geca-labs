
ALTER TABLE students
MODIFY COLUMN phone VARCHAR(20);
 
DESCRIBE students;
=======
-- Task 6: Rename Column
-- Rename 'name' column to 'student_name'

USE school_db;

-- TODO: Write your ALTER TABLE RENAME COLUMN command here
ALTER TABLE students 
RENAME COLUMN name TO student_name;
>>>>>>> 34f8c46e (Done)
