-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
-- INSERT INTO students (id, name, age, department) VALUES (...);


-- Query 2: Select all students
-- SELECT * FROM students;


-- Query 3: Select only names and departments
-- SELECT name, department FROM students;


-- Query 4: Select students from CSE department
-- SELECT * FROM students WHERE ...;


-- Query 5: Count total students
-- SELECT COUNT(*) as total FROM students;


-- Query 6: Count students per department
-- SELECT department, COUNT(*) as count FROM students GROUP BY ...;


-- Query 7: Find oldest student
-- SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
INSERT INTO students (id, name, age, department) VALUES
(101, 'Rahul Sharma', 20, 'CSE'),
(102, 'Sneha Patil', 19, 'IT'),
(103, 'Amit Verma', 21, 'ECE'),
(104, 'Priya Singh', 22, 'MECH'),
(105, 'Karan Mehta', 20, 'CSE');

SELECT * FROM students;

SELECT name, department FROM students;

SELECT * FROM students WHERE department = 'CSE';

SELECT COUNT(*) AS total FROM students;

SELECT department, COUNT(*) AS count 
FROM students 
GROUP BY department;

SELECT * FROM students 
WHERE age = (SELECT MAX(age) FROM students);