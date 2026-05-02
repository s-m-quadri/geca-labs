-- Lab 0: Basic SQL Queries
-- Task: Insert data and perform basic queries

USE student_db;

-- TODO: Complete the following queries

INSERT INTO students VALUES 
    (1, 'Alice Johnson', 20, 'CSE'),
    (2, 'Bob Smith', 21, 'ECE'),
    (3, 'Charlie Brown', 19, 'CSE'),
    (4, 'Diana Prince', 22, 'MECH'),
    (5, 'Eve Adams', 20, 'EEE');

SELECT * FROM students;
SELECT name, department FROM students;
SELECT * FROM students WHERE department = 'CSE';
SELECT COUNT(*) as total FROM students;
SELECT department, COUNT(*) as count FROM students GROUP BY department;
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
