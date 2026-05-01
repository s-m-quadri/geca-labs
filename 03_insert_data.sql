-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

INSERT INTO students VALUES ('Suhani', 19, '7th');

INSERT INTO students VALUES ('Dilip', 59, '7th');


-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);

<<<<<<< HEAD

 
=======
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(100)
);
>>>>>>> de8a6c3a (done)
