-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
-- INSERT INTO students (id, name, age, department) VALUES (...);

INSERT INTO students (id, name, age, department) VALUES (1, "pankaj", 20, "CSE"), (2, "Aditya", 19, "CSE"), (3, "Rohan", 19, "CSE");
INSERT INTO students (id, name, age, department) VALUES (4, "George", 20, "IT");


-- Query 2: Select all students
-- SELECT * FROM students;

SELECT * FROM students;


-- Query 3: Select only names and departments
-- SELECT name, department FROM students;

SELECT name, department FROM students;


-- Query 4: Select students from CSE department
-- SELECT * FROM students WHERE ...;

SELECT * FROM students WHERE department = "IT";

-- Query 5: Count total students
-- SELECT COUNT(*) as total FROM students;

SELECT COUNT(*) as total_students FROM students;


-- Query 6: Count students per department
-- SELECT department, COUNT(*) as count FROM students GROUP BY ...;

SELECT department, COUNT(*) as count FROM students GROUP BY department;


-- Query 7: Find oldest student
-- SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);

SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
