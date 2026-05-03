-- Task 5: Modify Column
-- Change 'age' column to be TINYINT with NOT NULL constraint

USE school_db;

-- TODO: Write your ALTER TABLE MODIFY COLUMN command here
INSERT INTO students(id,name,age,email)VALUES
(1,'Prince',20,'prince99@gmail.com'),
(2,'Rajeev',21,'rajeev69@gmail.com'),
(3,'Ishan',20,'Ishan@yahoo.com'),
(4,'Pranit',19,'pranitmore@yahoo.com');
SELECT * FROM students;