-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- Insert data
INSERT INTO students VALUES (1, 'Mayur', 20, 'CSE');
INSERT INTO students VALUES (2, 'Rohan', 20, 'IT');
INSERT INTO students VALUES (3, 'Rashi', 19, 'IT');
INSERT INTO students VALUES (4, 'Ravan', 21, 'CSE');
 
-- Select all
SELECT * FROM students;
 
-- Filter by department
SELECT * FROM students WHERE department = 'CSE';