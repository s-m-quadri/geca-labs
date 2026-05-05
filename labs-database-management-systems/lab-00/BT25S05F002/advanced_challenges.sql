USE teachers;
USE school_db;
-- CREATE TABLE teachers_tables(
--     teacher_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(50) NOT NULL,
--     emial VARCHAR (100) UNIQUE,
--     subject VARCHAR(50),
--     salary DECIMAL(10,2) DEFAULT 300000.00
-- );

-- desc teachers_tables;

-- ALTER TABLE students
-- ADD COLUMN teacher_id INT;

ALTER TABLE students
ADD FOREIGN KEY(teacher_id) REFERENCES teachers_tables(teacher_id);