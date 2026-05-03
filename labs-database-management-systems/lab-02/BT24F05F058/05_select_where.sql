-- Task 5: Select with WHERE
-- Find students in 10th grade

USE school_db;

-- TODO: SELECT students WHERE grade = '10th'

USE school_db;
INSERT INTO students (name, age, grade) VALUES ('Alice', 15, '10th');
INSERT INTO students (name, age, grade) VALUES
('Bob', 16, '11th'),
('Charlie', 15, '10th'),
('Diana', 17, '12th');  

SELECT * FROM students WHERE grade = '10th';
