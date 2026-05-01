-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
INSERT INTO students (id, name, age, department, cgpa) VALUES (101, 'Alice', 20, 'CSE', 8.5);
INSERT INTO students (id, name, age, department, cgpa) VALUES (102, 'Bob', 21, 'ECE', 7.8);
INSERT INTO students (id, name, age, department, cgpa) VALUES (103, 'Charlie', 19, 'ME', 8.2);
INSERT INTO students (id, name, age, department, cgpa) VALUES (104, 'Diana', 20, 'CSE', 8.9);
INSERT INTO students (id, name, age, department, cgpa) VALUES (105, 'Eve', 22, 'ECE', 7.9);

-- Query 2: Select all students
SELECT '=== All Students ===' AS query_title;
SELECT * FROM students;

-- Query 3: Select only names and departments
SELECT '=== Names and Departments ===' AS query_title;
SELECT name, department FROM students;

-- Query 4: Select students from CSE department
SELECT '=== CSE Department Students ===' AS query_title;
SELECT * FROM students WHERE department = 'CSE';

-- Query 5: Count total students
SELECT '=== Total Students Count ===' AS query_title;
SELECT COUNT(*) as total_students FROM students;

-- Query 6: Count students per department
SELECT '=== Students per Department ===' AS query_title;
SELECT department, COUNT(*) as student_count FROM students GROUP BY department ORDER BY student_count DESC;

-- Query 7: Find oldest student
SELECT '=== Oldest Student ===' AS query_title;
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);

-- Query 8: Students with CGPA > 8.0 sorted by CGPA
SELECT '=== High Performers (CGPA > 8.0) ===' AS query_title;
SELECT name, department, cgpa FROM students WHERE cgpa > 8.0 ORDER BY cgpa DESC;
