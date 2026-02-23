USE school_db;
ALTER TABLE students
ADD COLUMN email VARCHAR(200);

ALTER TABLE students 
ADD COLUMN phone VARCHAR(15);

DESCRIBE students;