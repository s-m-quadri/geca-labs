-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db; -- If this is commented the u need cmd as "sudo mysql school_db < 03_insert_data.sql"

-- TODO: Write your INSERT commands here
-- Example: INSERT INTO students VALUES (...);
INSERT INTO students(id,name,age,email)
VALUES 
(60,"kapil",20,"bt24f05f060@geca.ac.in"),
(41,"meeran",20,"bt24f05f041@geca.ac.in");

SELECT * FROM students;
