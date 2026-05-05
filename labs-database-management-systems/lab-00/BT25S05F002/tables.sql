

USE student_db;


CREATE TABLE students (
    id int primary key,
    name VARCHAR(50),
    age int,
    department varchar(50)
);

-- Verify table creation
DESCRIBE students;
