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

--ans:

USE student_db;
INSERT INTO students (id, name, age, department) VALUES (1, 'Alice', 20, 'CSE');
INSERT INTO students (id, name, age, department) VALUES (2, 'Bob', 21, 'ECE');
INSERT INTO students (id, name, age, department) VALUES (3, 'Charlie', 19, 'MECH');
INSERT INTO students (id, name, age, department) VALUES (4, 'David', 22, 'CSE');
INSERT INTO students (id, name, age, department) VALUES (5, 'Eve', 20, 'ECE');
SELECT * FROM students;
SELECT name, department FROM students;
SELECT * FROM students WHERE department = 'CSE';
SELECT COUNT(*) as total FROM students;
SELECT department, COUNT(*) as count FROM students GROUP BY department;
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);