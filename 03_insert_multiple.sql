USE school_db;

INSERT INTO students (name, age, grade) VALUES
('Bob', 16, '11th'),
('Charlie', 15, '10th'),
('Diana', 17, '12th'),
('Eve', 16, '11th');
 
SELECT * FROM students;
SELECT COUNT(*) as total FROM students;