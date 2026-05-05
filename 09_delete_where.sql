USE school_db;

-- See who will be deleted
SELECT * FROM students
WHERE age < 15;

-- Delete students younger than 15
DELETE FROM students
WHERE age < 15;

-- Check result
SELECT * FROM students;