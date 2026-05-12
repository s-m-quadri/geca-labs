USE school_db;
-- Always SELECT first to confirm which rows you are deleting
SELECT * FROM students WHERE id = 3;
DELETE FROM students WHERE id = 3;
SELECT * FROM students;