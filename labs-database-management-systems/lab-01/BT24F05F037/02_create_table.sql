-- Task 2: Create Students Table
-- Create table 'students' with: id, name, age, email

-- Switch to school_db
USE school_db;
create table students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE  
);



-- TODO: Write your CREATE TABLE command here
SELECT * FROM students; -- This line is just to verify the table creation, you can remove it if not needed.