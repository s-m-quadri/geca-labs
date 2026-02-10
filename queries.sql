-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
INSERT INTO students VALUES (11, 'Alice', 20, 'CSE');
INSERT INTO students VALUES (12, 'Nolan', 21, 'MECH');
INSERT INTO students VALUES (13, 'Jimmy', 22, 'ENTC');
INSERT INTO students VALUES (14, 'Chris', 23, 'CSE');
INSERT INTO students VALUES (15, 'Tony', 24, 'CE');



-- Query 2: Select all students
 SELECT * FROM students;


-- Query 3: Select only names and departments
SELECT name, department FROM students;


-- Query 4: Select students from CSE department
SELECT * FROM students WHERE department='CSE';


-- Query 5: Count total students
SELECT COUNT(*) as total FROM students;


-- Query 6: Count students per department
SELECT department, COUNT(*) as count FROM students GROUP BY name;


-- Query 7: Find oldest student
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
