-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
INSERT INTO students (id, name, age, department) VALUES (23,"anushka",20,"cse");
INSERT INTO students (id, name, age, department) VALUES (24,"Shreya",20,"civil");
INSERT INTO students (id, name, age, department) VALUES (25,"Dhiraj",21,"it");
INSERT INTO students (id, name, age, department) VALUES (26,"Harshada",19,"electrical");
INSERT INTO students (id, name, age, department) VALUES (27,"Harshad",22,"electrical");

-- Query 2: Select all students
SELECT * FROM students;


-- Query 3: Select only names and departments
SELECT name, department FROM students;


-- Query 4: Select students from CSE department
SELECT * FROM students WHERE department = "cse";


-- Query 5: Count total students
SELECT COUNT(*) as total FROM students;


-- Query 6: Count students per department
SELECT department, COUNT(*) as count FROM students GROUP BY department;


-- Query 7: Find oldest student
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
