
USE student_db;
-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries
-- TODO: Complete the following queries

-- Query 1: Insert at least 5 student records
-- INSERT INTO student (id, name, age, department) VALUES (1,"anjali",20,"cse");
-- INSERT INTO student (id, name, age, department) VALUES (2,"sneha", 20,"cse");

-- Query 2: Select all students
-- SELECT * FROM student;


-- Query 3: Select only names and departments
-- SELECT name, department FROM student;


-- Query 4: Select students from CSE department
-- SELECT * FROM student WHERE department = "CSE";


-- Query 5: Count total students
-- SELECT COUNT(*) as total FROM students;


-- Query 6: Count students per department
-- SELECT department, COUNT(*) as count FROM student GROUP BY department;


-- Query 7: Find oldest student
 SELECT * FROM student WHERE age = (SELECT MAX(age) FROM student);
