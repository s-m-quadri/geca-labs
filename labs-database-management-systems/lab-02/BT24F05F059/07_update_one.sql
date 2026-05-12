USE school_db;
-- Confirm before updating
SELECT * FROM students WHERE id = 1;
UPDATE students SET age = 16 WHERE id = 1;
SELECT * FROM students WHERE id = 1;