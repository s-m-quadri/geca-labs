
USE student_db;

DROP TABLE IF EXISTS students;

CREATE TABLE if NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(30)
);