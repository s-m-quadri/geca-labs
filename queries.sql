-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- Query 1: Insert at least 5 student records
INSERT INTO students (id, name, age, department) VALUES
(101, 'Alice', 20, 'CSE'),
(102, 'Bob', 21, 'ECE'),
(103, 'Charlie', 22, 'ME'),
(104, 'Diana', 19, 'CSE'),
(105, 'Ethan', 23, 'CE');

-- Query 2: Select all students
SELECT * FROM students;

-- Query 3: Select only names and departments
SELECT name, department FROM students;

-- Query 4: Select students from CSE department
SELECT * FROM students WHERE department = 'CSE';

-- Query 5: Count total students
SELECT COUNT(*) AS total FROM students;

-- Query 6: Count students per department
SELECT department, COUNT(*) AS count FROM students GROUP BY department;

-- Query 7: Find oldest student
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
