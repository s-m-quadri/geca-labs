-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);

INSERT INTO student_info(rollno,name,marks) VALUES(2,"BBB",19);
INSERT INTO student_info(rollno,name,marks) VALUES(3,"CCC",18);
SELECT * FROM student_info;
