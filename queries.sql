-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
INSERT INTO students (rollno, name, marks, dept) VALUES (101, "sayli", 20, "cse");


-- Query 2: Select all students
SELECT * FROM students;


-- Query 3: Select only names and departments
SELECT name, dept FROM students;


-- Query 4: Select students from CSE department
SELECT * FROM students WHERE rollno=101;


-- Query 5: Count total students
SELECT COUNT(*) as total FROM students;


-- Query 6: Count students per department



-- Query 7: Find oldest student
SELECT * FROM students WHERE marks = (SELECT MAX(marks) FROM students);
