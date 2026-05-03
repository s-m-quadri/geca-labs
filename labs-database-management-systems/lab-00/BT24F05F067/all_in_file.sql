CREATE DATABASE if NOT EXISTS student_db;

use student_db;


DROP TABLE IF EXISTS students;

CREATE TABLE if NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(30)
);

-- Insert data
INSERT INTO students VALUES (1, 'Mayur', 20, 'CSE');
INSERT INTO students VALUES (2, 'Rohan', 20, 'IT');
INSERT INTO students VALUES (3, 'Rashi', 19, 'IT');
INSERT INTO students VALUES (4, 'Ravan', 21, 'CSE');
 
-- Select all
SELECT * FROM students;
 