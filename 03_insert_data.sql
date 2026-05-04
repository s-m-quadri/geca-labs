
ALTER TABLE students
ADD PRIMARY KEY (id);
 
DESCRIBE students;
=======
-- Task 3: Insert Sample Data
-- Insert 3 student records into the students table

USE school_db;

-- TODO: Write your INSERT commands here
INSERT INTO students (id, name, age, email) VALUES 
(1, 'Alice Johnson', 20, 'alice.j@example.com'),
(2, 'Bob Smith', 22, 'bob.smith@example.com'),
(3, 'Charlie Davis', 21, 'charlie.d@example.com');
>>>>>>> 34f8c46e (Done)
