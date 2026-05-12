USE school_db;
-- Always SELECT first to confirm what will be deleted
SELECT * FROM students WHERE age < 15;
DELETE FROM students WHERE age < 15;
SELECT * FROM students;