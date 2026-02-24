-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;
INSERT INTO students (name, age, email, grade)
VALUES('Alice Johnson', 20, 'alice@gmail.com', 'A');
INSERT INTO students (name, age, email, grade)
VALUES('Bob Smith', 21, 'bob@gmail.com', 'B');
INSERT INTO students (name, age, email, grade)
VALUES('Charlie Brown', 19, 'charlie@gmail.com', 'A');
SELECT * FROM students;
