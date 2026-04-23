-- Task 6: Select with ORDER BY
-- Show students sorted by age (oldest first)

USE school_db;

-- TODO: SELECT all students ORDER BY age DESC
USE school_db;
INSERT INTO students (name, age, grade) VALUES
    ('Bob',     16, '11th'),
    ('Charlie', 15, '10th'),
    ('Diana',   17, '12th'),
    ('Eve',     16, '11th');
SELECT * FROM students;
SELECT COUNT(*) AS total FROM students;